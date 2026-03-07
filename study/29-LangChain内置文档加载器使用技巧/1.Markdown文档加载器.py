#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 安装依赖
# pip install unstructured
# pip install markdown

from langchain_community.document_loaders import UnstructuredMarkdownLoader

loader = UnstructuredMarkdownLoader("./项目API资料.md")
# mode= single或elements是有区别的，
# single表示整个markdown文档作为一个document
# elements表示每个markdown元素作为一个document，例如，每个标题、每个段落、每个列表项等都作为一个document，但一般不这样做，后续通过文本分割器进行分割而不是在加载的时候处理(无法保证不同文档分割操作的一致性，比如word和markdown文档分割维度不一样，可以先加载再分割)，因为加载时候分割是按元素类型分割的。
# loader = UnstructuredMarkdownLoader("./项目API资料.md", mode="elements")
# paged 是按页分割的，markdown默认只有一页，而word、excel等文档一般都有多个页
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
print(documents[0].page_content)

# 1.1 Markdown 文档加载器
# Markdown 是一种轻量级标记语言，可用于使用纯文本编辑器创建格式化文本。例如课程的电子书就是 Markdown 格式文件。
# LangChain 中封装了一个 unstructuredMarkdownLoader 对象，要使用这个加载器，必须安装 unstructured 包，安装命令：
# pip install unstructured

# unstructured 包是一款开源非结构化数据的预处理工具，旨在简化和优化结构化和非结构化文档的预处理，并且内置了用于读取和预处理图像和文本文档（如 PDF、HTML、Word 文档等）的开源组件。
# 也是 LangChain 文档加载器的核心（绝大部分加载器都基于 unstructured 包进行开发 + 封装）。

# 安装好 unstructured 包后，就可以和文本加载器一样，直接传递 Markdown 文档的路径，如下：
# from langchain_community.document_loaders import UnstructuredMarkdownLoader
# loader = UnstructuredMarkdownLoader("./LLMOps 项目 API 文档（资料）.md")
# documents = loader.load()
# print(documents)
# UnstructuredMarkdownLoader 默认会将整个文件加载到文档中，加载得到的文档列表只有一个元素，在这个元素的 page_content 中记录了整个 Markdown 文档的所有内容。
# 其实在幕后 unstructured 包的处理中，已经为不同的文本块创建了不同的 “元素”，默认情况下是全部结合到一起的，但是可以通过传递参数 mode="elements" 让所有元素全部分离。
