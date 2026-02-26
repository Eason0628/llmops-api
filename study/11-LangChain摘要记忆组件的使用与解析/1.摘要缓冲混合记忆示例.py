#!/usr/bin/env python
# @Time    : 2026-02-24 17:12
# @Author  : zhaowintoo@gmail.com
from operator import itemgetter

import dotenv
from langchain.memory import ConversationSummaryBufferMemory
from langchain_community.chat_models.baidu_qianfan_endpoint import QianfanChatEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

dotenv.load_dotenv()

# 1.创建提示模板&记忆
# 部分模型不支持传递多个消息角色为system，如果系统生成摘要，会有多个system消息，部分模型会报错，
# 所以使用记忆主键对接小众模型时要看源码是否支持对应封装，传递多条system消息
# 还有要注意不同模型的prompt的区别，为不同模型提供合适的prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据对应的上下文回复用户问题"),
    MessagesPlaceholder("history"),  # 需要的history其实是一个列表
    ("human", "{query}"),
])

memory = ConversationSummaryBufferMemory(
    max_token_limit=300,
    return_messages=True,
    input_key="query",
    llm=QianfanChatEndpoint(),
    # llm=ChatOpenAI(model="gpt-3.5-turbo-16k"),
)

# 2.创建大语言模型
# llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
llm = QianfanChatEndpoint()

# 3.构建链应用
chain = RunnablePassthrough.assign(
    history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
) | prompt | llm | StrOutputParser()

# 4.死循环构建对话命令行
while True:
    query = input("Human: ")

    if query == "q":
        exit(0)

    chain_input = {"query": query, "language": "中文"}

    response = chain.stream(chain_input)
    print("AI: ", flush=True, end="")
    output = ""
    for chunk in response:
        output += chunk
        print(chunk, flush=True, end="")
    memory.save_context(chain_input, {"output": output})
    print("")
    print("history: ", memory.load_memory_variables({}))
