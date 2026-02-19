# -*- coding: utf-8 -*-
# @Time    : 2026-02-18 20:51
# @Author  : zhaowintoo@gmail.com
# @File    : http_code.py
from enum import Enum


class HttpCode(str, Enum):
    """HTTP状态码"""
    SUCCESS = "success"  # 成功状态
    FAIL = "fail"  # 失败状态
    NOT_FOUND = "not_found"  # 未找到
    UNAUTHORIZED = "unauthorized"  # 未授权
    FORBIDDEN = "forbidden"  # 无权限
    VALIDATE_ERROR = "validate_error"  # 数据验证错误
