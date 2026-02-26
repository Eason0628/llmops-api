# -*- coding: utf-8 -*-
# @Time    : 2026-02-16 7:41
# @Author  : zhaowintoo@gmail.com
# @File    : app_handler.py

import os
import uuid
from dataclasses import dataclass
from operator import itemgetter

from injector import inject
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message


@inject
@dataclass
class AppHandler:
    """应用控制器"""

    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功获取，名字是{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改的名字是:{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，id为:{app.id}")

    # DeepSeek
    def debug(self, app_id: uuid.UUID):
        """聊天接口"""

        # 1.校验输入参数
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2.创建prompt与记忆
        prompt = ChatPromptTemplate.from_messages([
            ("system", "你是一个强大的聊天机器人，能根据用户的提问回复对应的问题"),
            # MessagesPlaceholder是一个占位符，用于在prompt中插入记忆
            MessagesPlaceholder("history"),
            ("human", "{query}"),
        ])
        # 3.创建记忆组件ConversationBufferWindowMemory(一种记忆组件)
        memory = ConversationBufferWindowMemory(
            k=3,
            input_key="query",
            output_key="output",
            return_messages=True,
            chat_memory=FileChatMessageHistory("./storage/memory/chat_history.txt"),
        )

        # 4.构建 LLM
        llm = ChatOpenAI(
            model="deepseek-chat",
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_BASE_URL"),
            temperature=0
        )

        # 5.输出解析器
        parser = StrOutputParser()

        # 6.构建链
        chain = (RunnablePassthrough.assign(
            # 这里是将memory.load_memory_variables的结果中的"history"键对应的值赋值给"history"键
            # | itemgetter("history")这里是将memory.load_memory_variables的结果中的"history"键对应的值提取出来传递给后续的prompt
            history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
        ) | prompt | llm | parser)

        # 7.调用链生成内容
        chain_input = {"query": req.query.data}
        content = chain.invoke(chain_input)
        #  保存用户的输入和模型的输出到记忆中
        memory.save_context(chain_input, {"output": content})
        # 8.返回结果
        return success_json({"content": content})

    # OPENAI
    # def completion(self):
    #     """聊天接口"""
    #     print("completion is called")
    #     # 1.从接口中获取输入
    #     data = request.get_json()
    #     query = data.get("query")
    #     # 2.创建openai客户端，并发起请求
    #     client = OpenAI(
    #     )
    #     resp = client.responses.create(
    #         model="gpt-5.2",
    #         input=[
    #             {"role": "system", "content": "你是OPENAI开发的聊天机器人，请根据用户的输入回复对应的信息"},
    #             {"role": "user", "content": query},
    #         ],
    #     )
    #     # 3.得到请求结果，然后将openai的结果返回给前端
    #     return jsonify({"answer": resp.output_text})

    def ping(self):
        """测试应用"""
        # raise FailException("failException")
        return {"ping": "pong"}
