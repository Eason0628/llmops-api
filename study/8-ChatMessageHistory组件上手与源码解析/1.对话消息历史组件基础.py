#!/usr/bin/env python
# @Time    : 2026-02-24 17:12
# @Author  : zhaowintoo@gmail.com
# @File    : 1.对话消息历史组件基础.py
from langchain_core.chat_history import InMemoryChatMessageHistory

chat_history = InMemoryChatMessageHistory()

chat_history.add_user_message("你好，我是Eason，你是谁？")
chat_history.add_ai_message("你好，我是ChatGPT，有什么可以帮到您的？")

# print(chat_history)
print(chat_history.messages)
