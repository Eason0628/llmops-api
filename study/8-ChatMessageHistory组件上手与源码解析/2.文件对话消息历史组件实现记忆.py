#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026-02-24 17:12
# @Author  : zhaowintoo@gmail.com
# @File    : 2.文件对话消息历史组件实现记忆.py
import dotenv
from langchain_community.chat_message_histories import FileChatMessageHistory
from openai import OpenAI

dotenv.load_dotenv()

# 1.创建客户端&记忆
client = OpenAI(api_key="***", base_url="https://api.deepseek.com")
chat_history = FileChatMessageHistory("./memory.txt")

# 2.循环对话
while True:
    # 3.获取用户的输入
    query = input("Human: ")

    # 4.检测用户是否退出对话
    if query == "q":
        exit(0)

    # 5.发起聊天对话
    print("AI: ", flush=True, end="")
    system_prompt = (
        "你是深度求索开发的Deepseek聊天机器人，可以根据相应的上下文回复用户信息，上下文里存放的是人类与你对话的信息列表。\n\n"
        f"<context>{chat_history}</context>\n\n"
    )
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        stream=True,
    )
    ai_content = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break
        ai_content += content
        print(content, flush=True, end="")
    # 6.将用户的输入和AI的回复添加到记忆中
    chat_history.add_user_message(query)
    chat_history.add_ai_message(ai_content)
    print("")

# 即使重启程序，因为文件记忆组件是基于文件的，所以重启程序后，记忆组件会优先读取文件中的内容，恢复之前的对话记录。
# 不同的prompt在不同的模型会有不同的效果,所以在使用不同的模型时,需要根据模型的特点,调整prompt,从而实现最佳的效果,大语言引用开发实际上是开发prompt,为不同的大语言模型配置不同的prompt,从而实现不同的功能。
# 上面的案例会将每次的对话记录都添加到文件中,所以在使用文件记忆组件时,需要注意文件的大小(Token消耗多、回复慢问题),避免文件过大导致性能问题。
