#!/usr/bin/env python
# -*- coding: utf-8 -*-

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    cache_folder="./embeddings/"
    # 安装插件pip install -U langchain-huggingface sentence-transformers
    # 当我们配置模型名字和缓存文件夹的时候，就会自动到huggingface官网下载模型，
    # 当指定文件夹下./embeddings/有模型的时候，就不需要https://huggingface.co下载模型了，
    # 程序就直接去读取本地的这个文件，然后去导入对应的模型，创建对应的文本嵌入。
    # model_name + cache_folder也可以将公司内部开发的文本嵌入模型，进行配置，然后进行使用。
)

query_vector = embeddings.embed_query("你好，我是Eason，我喜欢打篮球游泳")

print(query_vector)
print(len(query_vector))
