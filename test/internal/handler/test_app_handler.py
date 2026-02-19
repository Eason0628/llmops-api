# -*- coding: utf-8 -*-
# @Time    : 2026-02-19 7:35
# @Author  : zhaowintoo@gmail.com
# @File    : test_app_handler.py
import pytest

from pkg.response import HttpCode


class TestAppHandler():
    """测试应用处理器"""

    # [None, "你好，你是谁?"]代表可以传递空字符串或正常字符串
    @pytest.mark.parametrize("query", [None, "你好，你是谁?"])
    def test_completion(self, query, client):
        resp = client.post("/app/completion", json={"query": query})
        assert resp.status_code == 200
        # 通过断言测试两种参数的情况
        if query is None:
            assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
        print('响应内容:', resp.json)
