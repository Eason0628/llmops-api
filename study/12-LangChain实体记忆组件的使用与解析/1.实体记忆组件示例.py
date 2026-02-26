#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026-02-26 8:43
# @Author  : zhaowintoo@gmail.com
# @File    : 1.实体记忆组件示例.py
# 先了解实体记忆组件就可以了，后续会通过函数回调的方式提取整个会话历史中对应的实体的关键字，为实体关键字提供总结描述，性能更好适用范围更广

import dotenv
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain_community.chat_models.baidu_qianfan_endpoint import QianfanChatEndpoint

dotenv.load_dotenv()

# llm = ChatOpenAI(model="gpt-4o", temperature=0)
llm = QianfanChatEndpoint()

chain = ConversationChain(
    llm=llm,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=ConversationEntityMemory(llm=llm),
)

print(chain.invoke({"input": "你好，我是Eason。我最近正在学习LangChain。"}))
print(chain.invoke({"input": "我最喜欢的编程语言是 Python。"}))
print(chain.invoke({"input": "我住在广州"}))

# 查询实体中的对话
res = chain.memory.entity_store.store
print(res)
