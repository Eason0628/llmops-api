#!/usr/bin/env python
# -*- coding: utf-8 -*-
from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader

loader = FileSystemBlobLoader(".", show_progress=True, glob="*.txt")

for blob in loader.yield_blobs():
    print(blob.source)
    # print(blob.as_string())
