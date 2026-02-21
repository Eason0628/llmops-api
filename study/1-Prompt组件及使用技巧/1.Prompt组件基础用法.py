#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from langchain_core.messages import AIMessage
from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
prompt_value = prompt.invoke({"subject": "程序员"})
print(prompt.format(subject="喜剧演员"))
print(prompt_value.to_string())
print(prompt_value.to_messages())

print("==================")

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，当前的时间为:{now}"),
    # 有时候可能还有其他的消息，但是不确定
    MessagesPlaceholder("chat_history"),
    HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话"),
]).partial(now=datetime.now())
# partial 方法可以为模板填充一些固定的参数，返回的是一个还是模板
# invoke 调用的时候必须赋值所有的参数，返回的是一个 PromptValue 对象，包含了所有的消息,这个是它们两个的区别
chat_prompt_value = chat_prompt.invoke({
    "chat_history": [
        ("human", "我叫雷军"),
        AIMessage("你好，我是ChatGPT，有什么可以帮到您"),
    ],
    "subject": "程序员",
})
# 打印可以看到区别
print(chat_prompt_value)
print(chat_prompt_value.to_string())
