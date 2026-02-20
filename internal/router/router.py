# -*- coding: utf-8 -*-
# @Time    : 2026-02-16 7:51
# @Author  : zhaowintoo@gmail.com
# @File    : router.py
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject  # 依赖注入
@dataclass  # 无论路由下有多少个控制器，都会被自动注册到路由中，起到手动__init__构造函数逐个写控制器的作用
class Router:
    app_handler: AppHandler

    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    """注册路由"""

    def register_router(self, app: Flask):
        # 1.创建一个蓝图(蓝图是一个容器，用于存放路由和视图函数)
        # 第一个参数是整个蓝图的名称，第二个参数是所在的模块，第三个参数是路由的前缀
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2.将url和对应的控制器方法做绑定
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.completion)
        bp.add_url_rule("/app", methods=["POST"], view_func=self.app_handler.create_app)
        bp.add_url_rule("/app/<uuid:id>", view_func=self.app_handler.get_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["POST"], view_func=self.app_handler.update_app)
        bp.add_url_rule("/app/<uuid:id>/delete", methods=["POST"], view_func=self.app_handler.delete_app)

        # 3.将蓝图注册到app中
        app.register_blueprint(bp)
