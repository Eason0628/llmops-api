# -*- coding: utf-8 -*-
# @Time    : 2026-02-16 14:38
# @Author  : zhaowintoo@gmail.com
# @File    : app.py
from injector import Module, Binder

from internal.extension.database_extension import db
from pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
