#!/usr/bin/env python
# -*- coding: utf-8 -*-

from langchain_community.document_loaders import (
    UnstructuredPowerPointLoader,
)

# excel_loader = UnstructuredExcelLoader("./员工考勤表.xlsx", mode="elements")
# excel_documents = excel_loader.load()

# word_loader = UnstructuredWordDocumentLoader("./喵喵.docx")
# documents = word_loader.load()

ppt_loader = UnstructuredPowerPointLoader("./章节介绍.pptx")
documents = ppt_loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)

# 1.2 Office 文档加载器
# 除了 Markdown 文档，另外一种高频使用的数据就是 Office 文档，在 LangChain 中也基于 unstructured 包封装了对应的文档加载器 ——unstructuredExcelLoader、unstructuredPowerPointLoader、unstructuredWordDocumentLoader。
# 分别对应 Excel、PPT、Word 文档加载器，其中不同的加载器需要安装不同的 Python 包，命令如下：
# unstructuredExcelLoader加载器所需包
# pip install unstructured openpyxl pandas

# unstructuredPowerPointLoader加载器所需包
# pip install unstructured python-magic python-pptx

# unstructuredWordDocumentLoader加载器所需包
# pip install unstructured
# Office 类的非结构化文档加载器使用技巧都非常简单，一般来说，传递对应文档的路径即可，如果需要区分文档中的元素，可以在加载器的构造函数中传递 mode="elements" 即可（但是一般不使用）。
# 示例如下：
# from langchain_community.document_loaders import (
#     UnstructuredExcelLoader,
#     UnstructuredPowerPointLoader,
#     UnstructuredWordDocumentLoader,
# )
# excel_loader = UnstructuredExcelLoader("./员工考勤表.xlsx")
# ppt_loader = UnstructuredPowerPointLoader("./章节介绍.pptx", mode="elements")
# word_loader = UnstructuredWordDocumentLoader("./喵喵.docx")
