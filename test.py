# -*- coding: utf-8 -*-
# @Time    : 2026-02-16 7:29
# @Author  : zhaowintoo@gmail.com
# @File    : test.py

from injector import inject, Injector


class A:
    name: str = "A:LLMOPS"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A的Name: {self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
