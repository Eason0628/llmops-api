# -*- coding: utf-8 -*-
# @Time    : 2026-02-24 17:12
# @Author  : zhaowintoo@gmail.com
# @File    : 1.摘要缓冲混合记忆.py.py
from typing import Any

from openai import OpenAI


# 1.max_tokens用于判断是否需要生成新的摘要
# 2.summary用于存储摘要的信息
# 3.chat_histories用于存储历史对话
# 4.get_num_tokens用于计算传入文本的token数
# 5.save_context用于存储新的交流对话
# 6.get_buffer_string用于将历史对话转换成字符串
# 7.load_memory_variables用于加载记忆变量信息
# 8.summary_text用于将旧的摘要和传入的对话生成新摘要
class ConversationSummaryBufferMemory:
    """摘要缓冲混合记忆类"""

    def __init__(self, summary: str = '', chat_histories: list = None, max_tokens: int = 300):
        self.summary = summary
        self.chat_histories = [] if chat_histories is None else chat_histories
        self.max_tokens = max_tokens
        self._client = OpenAI(api_key="sk-1bdb8cb5c94847718cc4d0958bdd0d6d", base_url="https://api.deepseek.com")

    @classmethod
    def get_num_tokens(cls, query: str) -> int:
        """计算传入的query的token数"""
        return len(query)

    def save_context(self, human_query: str, ai_content: str) -> None:
        """保存传入的新一次对话信息"""
        self.chat_histories.append({"human": human_query, "ai": ai_content})

        buffer_string = self.get_buffer_string()

        tokens = self.get_num_tokens(buffer_string)

        if tokens > self.max_tokens:
            first_chat = self.chat_histories[0]
            print("新摘要生成中~")
            self.summary = self.summary_text(
                self.summary,
                f"Human:{first_chat.get('human')}\nAI:{first_chat.get('ai')}"
            )
            print("新摘要生成成功:", self.summary)
            del self.chat_histories[0]

    def get_buffer_string(self) -> str:
        """将历史对话转换成字符串"""
        buffer: str = ""
        for chat in self.chat_histories:
            buffer += f"Human:{chat.get('human')}\nAI:{chat.get('ai')}\n\n"
        return buffer.strip()

    def load_memory_variables(self) -> dict[str, Any]:
        """加载记忆变量为一个字典，便于格式化到prompt中"""
        buffer_string = self.get_buffer_string()
        return {
            "chat_history": f"摘要:{self.summary}\n\n历史信息:{buffer_string}\n"
        }

    def summary_text(self, origin_summary: str, new_line: str) -> str:
        """用于将旧摘要和传入的新对话生成一个新摘要"""
        prompt = f"""你是一个强大的聊天机器人，请根据用户提供的谈话内容，总结摘要，并将其添加到先前提供的摘要中，返回一个新的摘要，除了新摘要其他任何数据都不要生成，如果用户的对话信息里有一些关键的信息，比方说姓名、爱好、性别、重要事件等等，这些全部都要包括在生成的摘要中，摘要尽可能要还原用户的对话记录。

    请不要将<example>标签里的数据当成实际的数据，这里的数据只是一个示例数据，告诉你该如何生成新摘要。

    <example>
    当前摘要：人类会问人工智能对人工智能的看法，人工智能认为人工智能是一股向善的力量。

    新的对话：
    Human：为什么你认为人工智能是一股向善的力量？
    AI：因为人工智能会帮助人类充分发挥潜力。

    新摘要：人类会问人工智能对人工智能的看法，人工智能认为人工智能是一股向善的力量，因为它将帮助人类充分发挥潜力。
    </example>

    =====================以下的数据是实际需要处理的数据=====================

    当前摘要：{origin_summary}

    新的对话：
    {new_line}

    请帮用户将上面的信息生成新摘要。"""
        completion = self._client.chat.completions.create(
            model='deepseek-chat',
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content


# 1.创建openai客户端

client = OpenAI(
    api_key="sk-1bdb8cb5c94847718cc4d0958bdd0d6d",
    base_url="https://api.deepseek.com"
)
memory = ConversationSummaryBufferMemory("", [], 300)

# 2.创建一个死循环用于人机对话
while True:
    # 3.获取人类的输入
    query = input('Human: ')

    # 4.判断下输入是否为q，如果是则退出
    if query.lower() == 'q':
        break

    # 5.向openai的接口发起请求获取ai生成的内容
    memory_variables = memory.load_memory_variables()
    answer_prompt = (
        "你是一个强大的聊天机器人，请根据对应的上下文和用户提问解决问题。\n\n"
        f"{memory_variables.get('chat_history')}\n\n"
        f"用户的提问是: {query}"
    )

    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[
            {"role": "user", "content": answer_prompt},
        ],
        stream=True,
    )

    # 6.循环读取流式响应的内容
    print("AI: ", flush=True, end="")
    ai_content = ""

    for chunk in response:
        # DeepSeek流式返回时可能出现None，需要安全判断
        if not chunk.choices:
            continue

        delta = chunk.choices[0].delta
        if not delta:
            continue

        content = delta.content
        if content:
            ai_content += content
            print(content, flush=True, end="")

    print("")
    memory.save_context(query, ai_content)

"""
Human: 你好，我叫伊森，我喜欢打篮球，你是谁？你喜欢什么呢？
AI: 你好，伊森！很高兴认识你！我是一个人工智能助手，由深度求索公司创造，名字叫DeepSeek。我没有个人喜好或情感，但我的“兴趣”可以理解为帮助用户解决问题、提供信息或进行有趣的对话——比如和你聊聊篮球！
如果你愿意分享，我可以陪你讨论篮球技巧、赛事，或者任何你感兴趣的话题。你平时打什么位置？有喜欢的球星或球队吗？ 😊

Human: 你能用一段话简单介绍一下什么是LLM大语言模型吗？
AI: LLM（大语言模型）是一种基于深度学习的人工智能系统，通过在海量文本数据上进行训练，学会理解和生成人类语言。它能够根据输入的上下文进行对话、回答问题、创作文本或执行语言相关任务，其核心能力源于对语言规律和知识的统计学习。例如，像我这样的助手就是LLM的一种应用，旨在以自然、连贯的方式与用户交流并提供帮助。
新摘要生成中~
新摘要生成成功: 人类伊森喜欢打篮球，他向人工智能助手DeepSeek介绍了自己并询问对方的喜好。DeepSeek表示自己是由深度求索公司创造的人工智能，没有个人情感，但乐于帮助用户解决问题、提供信息并进行对话，例如讨论篮球技巧、赛事或相关话题，并询问伊森平时打什么位置以及是否有喜欢的球星或球队。
Human: 我叫伊森，你知道我喜欢什么么?
AI: 伊森你好！根据之前的对话，你提到过自己喜欢打篮球，还向我介绍了自己。虽然我无法记住历史信息，但根据当前上下文，我知道你曾分享过对篮球的兴趣。如果你愿意，我们可以继续聊聊篮球相关的话题，比如你常打的位置、喜欢的球星或球队，或者任何你想讨论的内容！ 😊
新摘要生成中~
新摘要生成成功: 人类伊森喜欢打篮球，他向人工智能助手DeepSeek介绍了自己并询问对方的喜好。DeepSeek表示自己是由深度求索公司创造的人工智能，没有个人情感，但乐于帮助用户解决问题、提供信息并进行对话，例如讨论篮球技巧、赛事或相关话题，并询问伊森平时打什么位置以及是否有喜欢的球星或球队。随后伊森询问LLM大语言模型的定义，DeepSeek解释LLM是一种基于深度学习的人工智能系统，通过在海量文本数据上训练来理解和生成人类语言，能够进行对话、回答问题、创作文本或执行语言任务，其核心能力源于对语言规律和知识的统计学习，并举例说明像自己这样的助手就是LLM的一种应用。
Human: q
"""
