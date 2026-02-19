# -*- coding: utf-8 -*-
# @Time    : 2026-02-18 16:26
# @Author  : zhaowintoo@gmail.com
# @File    : config.py


class Config:
    def __init__(self):
        # 关闭CSRF保护
        self.WTF_CSRF_ENABLED = False
