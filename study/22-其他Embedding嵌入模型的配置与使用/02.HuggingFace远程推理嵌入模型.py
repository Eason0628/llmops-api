#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import dotenv
from langchain_huggingface import HuggingFaceEndpointEmbeddings

dotenv.load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    endpoint_url="https://hf-mirror.com"
)

query_vector = embeddings.embed_query("你好，我是Ethan，我喜欢打篮球游泳")

print(query_vector)
print(len(query_vector))

# 所以如果想去测试文本嵌入模型，但是又不想下载下来，
# 我们就可以使用这种远程推理，测试好之后我们就可以将它部署到本地，或者是一直使用huggingface的服务也是可以的。
# 但是这样子使用它远程服务超过一定限制的时候，就需要去付费了。
