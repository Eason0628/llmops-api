# -*- coding: utf-8 -*-
# @Time    : 2026-02-16 14:38
# @Author  : zhaowintoo@gmail.com
# @File    : app.py
import dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http

# 将dotenv文件中的环境变量加载到环境变量中
dotenv.load_dotenv()
injector = Injector()
conf = Config()
app = Http(__name__, conf=conf, router=injector.get(Router))
if __name__ == "__main__":
    app.run(debug=True)
