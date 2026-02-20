# -*- coding: utf-8 -*-
# @Time    : 2026-02-16 7:41
# @Author  : zhaowintoo@gmail.com
# @File    : app_handler.py

import os
import uuid
from dataclasses import dataclass

from injector import inject
from openai import OpenAI

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
    def completion(self):
        """聊天接口"""
        # 1.从接口中获取输入,校验输入参数query
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2.创建openai客户端，并发起请求
        client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_BASE_URL"))
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是DeepSeek开发的聊天机器人，请根据用户的输入回复对应的信息"},
                {"role": "user", "content": req.query.data},
            ],
            stream=False
        )
        content = response.choices[0].message.content

        # 3.得到请求结果，然后将openai的结果返回给前端
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
