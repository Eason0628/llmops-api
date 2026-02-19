# -*- coding: utf-8 -*-
# @Time    : 2026-02-18 15:58
# @Author  : zhaowintoo@gmail.com
# @File    : app_schema.py
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求验证"""
    # 必填、长度最大为2000
    query = StringField("query", validators=[
        DataRequired(message="用户提问是必填项"),
        Length(max=2000, message="用户提问最大长度是2000")
    ])
