from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader

import asyncio

async def document_loading(temp_path, file_type, ext):
    if file_type=="text-pdf" and ext==".pdf":
        loader=PyPDFLoader(temp_path)
        doc=await asyncio.wait_for(asyncio.to_thread(loader.load),timeout=30)
        return doc
    elif file_type=="text-file" and ext==".txt":
        loader=TextLoader(temp_path)
        doc=await asyncio.wait_for(asyncio.to_thread(loader.load),timeout=30)
        return doc 
    elif file_type=="text-file" and ext==".docx":
        loader=Docx2txtLoader(temp_path)
        doc=await asyncio.wait_for(asyncio.to_thread(loader.load),timeout=30)
        return doc
    