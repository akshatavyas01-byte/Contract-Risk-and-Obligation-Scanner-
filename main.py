from fastapi import FastAPI,UploadFile, File, Query
from fastapi.responses import StreamingResponse
import tempfile
from functions import document_loading 
from langchain_text_splitters import CharacterTextSplitter
from LLM import chain, chain2
import os
app=FastAPI()

async def Stream(temp_path:str, ext:str , filetype:str ):
    full_data=""
    chunk_data=""
    splitter=CharacterTextSplitter(chunk_size=1500, chunk_overlap=500, separator="\n\n")
    yield f"Document Loading right now please wait..................................\n\n"
    text= await document_loading(temp_path, ext,filetype)
    if text=="NOT SATISFACTORY DATA":
        yield "NOT SATISFACTORY DATA"
    else:
        chunks=splitter.split_text(text)
        for chunk in chunks:
            try:
                for data in chain.stream({"data":chunk}):
                    yield data
                    chunk_data+=data+"\n"
                full_data+=chunk_data
            except Exception as e:
                yield e 
    try:
        for chunk in chain2.stream({"risk":chunk_data}):
            yield chunk
    except Exception as e:
        yield e

    

@app.post("/stream/")
async def Streaming(
        file:UploadFile,
        filetype=Query(str)
):
    if file and filetype:
        ext=os.path.splitext(file.filename)[1] if file.filename else ".pdf"
        with tempfile.NamedTemporaryFile(delete=False,suffix=ext) as temp:
            content=await file.read()
            temp.write(content)
            temp_path=temp.name     
        return StreamingResponse(Stream(temp_path,ext,filetype),media_type="text/event-stream")