#!/usr/bin/env python
# -*- coding: utf-8 -*-
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.bilibili.com")
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)

# 1.3 URL 网页加载器
# 除了本地文件，LangChain 还封装了大量加载网络文件的加载器，例如：网页加载器、腾讯云 COS 对象存储加载器、Bilibili 字幕加载器、Notion 数据库加载器等等，使用技巧和文件加载器大差不差，传递对应的信息构建加载器，然后加载文档即可。
# 例如如果想加载获取B站网站首页的数据，即可使用 webBaseLoader 一键加载，示例如下：
# from langchain_community.document_loaders import webBaseLoader
# loader = webBaseLoader("https://www.bilibili.com")
# documents = loader.load()
# print(documents)

# WebBaseLoader 加载器底层会从 HTML 网页中加载所有文本（去除 HTML 标签），并将所有文本进行合并。利用这个加载器其实就可以快速实现一个基于特定网页问答的聊天机器人。
# WebBaseLoader 加载器翻译文档：https://imooc-langchain.shortvar.com/docs/integrations/document_loaders/web_base/
