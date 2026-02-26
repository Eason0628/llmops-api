#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026-02-24 17:12
# @Author  : zhaowintoo@gmail.com
# @File    : BaseChatMemory运行流程解析.py
from langchain.memory import BaseChatMemory

memory = BaseChatMemory(
    input_key="query",
    output_key="output",
    return_messages=True,
    # chat_history 假设
)

# 1. 加载记忆变量
memory_variable = memory.load_memory_variables({})
# 2. 调用模型
# content = chain.invoke({"query": "你好，我是Eason你是谁", "chat_history": memory_variable.get("chat_history")})
# 3. 保存上下文
# memory.save_context({"query": "你好，我是Eason你是谁"}, {"output": "你好，我是ChatGPT,有什么可以帮到您的"})
memory_variable = memory.load_memory_variables({})
# content = chain.invoke({"query": "你好，我是Eason你是谁", "chat_history": memory_variable.get("chat_history")})
