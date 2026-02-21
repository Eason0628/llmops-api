#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/6/9 18:59
@Author  : zhaowintoo@gmail.com
@File    : 2.Model批处理.py
"""
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# llm.batch是批量处理的方法，它可以一次处理多个输入，返回多个输出
# 作用是当某个大模型不支持一条prompt生成多条输出时，我们可以使用llm.batch方法来模拟批量处理
# 如果某个大模型不支持一条prompt生成多条输出支持的话可以 llm = ChatOpenAI(model="gpt-3.5-turbo-16k",n=2)
ai_messages = llm.batch([
    prompt.invoke({"query": "你好，你是?"}),
    prompt.invoke({"query": "请讲一个关于程序员的冷笑话"}),
])

for ai_message in ai_messages:
    print(ai_message.content)
    print("====================")
