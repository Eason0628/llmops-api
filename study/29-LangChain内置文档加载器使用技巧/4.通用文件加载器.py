#!/usr/bin/env python
# -*- coding: utf-8 -*-

from langchain_community.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("./项目API资料.md")
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)

# 通用文件加载器的使用技巧
# 在实际的 LLM 应用开发中，由于数据的种类是无穷的，没办法单独为每一种数据配置一个加载器（也不现实），所以对于一些无法判断的数据类型或者想进行通用性文件加载，可以统一使用非结构化文件加载器 UnstructuredFileLoader 来实现对文件的加载。
# UnstructuredFileLoader 是所有 UnstructuredXxxLoader 文档类的基类，其核心是将文档划分为元素，当传递一个文件时，库将读取文档，将其分割为多个部分，对这些部分进行分类，然后提取每个部分的文本，然后根据模式决定是否合并（single、paged、elements）。
# 一个 UnstructuredFileLoader 可以加载多种类型的文件，涵盖了：文本文件、PowerPoint 文件、HTML、PDF、图像、Markdown、Excel、Word 等，使用示例如下：
# 使用示例
# from langchain_community.document_loaders import UnstructuredFileLoader
# loader = UnstructuredFileLoader("./章节介绍.pptx")
# documents = loader.load()
# print(documents)
# 输出示例：
# plaintext
# [Document(page_content='LangChain RAG应用开发组件深入学习\n\n章节介绍\n\nLangChain文档组件与文档加载器\n\n学习了解Document组件在RAG应用开发中的作用，并学习LangChain文档加载器的配置与使用。\n\n学习掌握LangChain集成的各类文档加载器，涵盖CSV文件加载、HTML网页加载、PDF/文件夹/Markdown加载器以及通用文件加载器的使用。\n\n学习掌握封装LangChain自定义文档加载器的使用。\n\nLangChain文档转换器与分割器\n\n学习了解LangChain文档转换器的作用与使用场景，涵盖了拆分、合并、过滤、翻译等多个功能。\n\n学习掌握LangChain集成的各类文本分割器的使用以及封装自定义文本分割器的技巧，不同模式下选择分割器的思路。\n\n学习掌握LangChain语义分割器的使用及运行流程，以及语义分割器的使用场合。\n\nvectorStore组件与检索器的使用\n\n深入学习vectorStore组件，了解多种相似性搜索的几何意义以及在不同场合下的选择策略。\n\n学习掌握LangChain检索器与第三方检索器的配置与使用。\n\n学习掌握自定义LangChain检索器的技巧。', metadata={'source': './章节介绍.pptx'})]


# 不过由于 UnstructuredFileLoader 加载器提取元数据只记录了 source 即数据的来源，信息相对较少，所以如果能明确文件的类型，亦或者是一些高频的文件，尽可能使用更精确的文档加载器，记录的内容会更丰富。
# 例如通过检测文件的扩展名来加载不同的文件加载器，对于没校验到的文件类型，才考虑使用 UnstructuredFileLoader，如下：5.
# if file_extension in [".xlsx", ".xls"]:
#     loader = UnstructuredExcelLoader(file_path)
# elif file_extension == ".pdf":
#     loader = UnstructuredPDFLoader(file_path)
# elif file_extension in [".md", ".markdown"]:
#     loader = UnstructuredMarkdownLoader(file_path)
# elif file_extension in [".htm", "html"]:
#     loader = UnstructuredHTMLLoader(file_path)
# elif file_extension in [".docx", ".doc"]:
#     loader = UnstructuredWordDocumentLoader(file_path)
# elif file_extension == ".csv":
#     loader = UnstructuredCSVLoader(file_path)
# elif file_extension in [".ppt", ".pptx"]:
#     loader = UnstructuredPowerPointLoader(file_path)
# elif file_extension == ".xml":
#     loader = UnstructuredXMLLoader(file_path)
