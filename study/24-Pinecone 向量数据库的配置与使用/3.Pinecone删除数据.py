#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

dotenv.load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="shibing624/text2vec-base-chinese",
    cache_folder="./embeddings/"
)

db = PineconeVectorStore(index_name="llmops", embedding=embedding, namespace="dataset")

# 删除指定id的数据
# id = "4fb3c826-a381-41e2-ab2f-49ef4fed663b"
# db.delete([id], namespace="dataset")

# 更新指定id的数据
# langchain没有提供update方法，只能通过pinecone的api获取id对应的向量，然后更新
# pinecone_index = db.get_pinecone_index("llmops")
# pinecone_index.update(id="xxx", values=[], metadata={}, namespace="xxx")
