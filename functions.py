from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader
from langchain_classic.schema import Document
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

import asyncio

async def document_loading(temp_path:str, ext:str, file_type:str):
    if file_type=="text-pdf" and ext==".pdf":
        loader=PyPDFLoader(temp_path)
        doc=await asyncio.wait_for(asyncio.to_thread(loader.load),timeout=30)
        extracted_text=""
        for d in doc:
            extracted_text=("\n").join(d.page_content)
        return extracted_text
    elif file_type=="text-file" and ext==".txt":
        loader=TextLoader(temp_path)
        doc=await asyncio.wait_for(asyncio.to_thread(loader.load),timeout=30)
        extracted_text=""
        for d in doc:
            extracted_text=("\n").join(d.page_content)
        return extracted_text
    elif file_type=="text-file" and ext==".docx":
        loader=Docx2txtLoader(temp_path)
        doc=await asyncio.wait_for(asyncio.to_thread(loader.load),timeout=30)
        extracted_text=""
        for d in doc:
            extracted_text=("\n").join(d.page_content)
        return extracted_text
    elif file_type=="image-pdf" and ext==".pdf":
        images=convert_from_path(temp_path)
        extracted_text=""
        for image in images:
            text=pytesseract.image_to_string(image)
            extracted_text+=text+"\n"     
        return extracted_text
    else:
        return "NOT SATISFACTORY DATA"
    
    