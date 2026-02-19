from fastapi import FastAPI,UploadFile, File, Query
from fastapi.responses import StreamingResponse
import tempfile
from functions import document_loading 
from LLM import chain
import os
app=FastAPI()

async def Stream(temp_path:str, ext:str , filetype:str ):
    yield f"Document Loading right now please wait..................................\n\n"
    text= await document_loading(temp_path, ext,filetype)
    if text=="NOT SATISFACTORY DATA":
        yield "NOT SATISFACTORY DATA"
    else:
        for chunk in chain.stream({"data":text}):
            yield chunk
    

@app.post("/stream/")
async def Streaming(
        file:UploadFile,
        filetype=Query(str)
):
    if file and filetype:
        ext=os.path.splitext(file.filename)[1] if file.filename else ".pdf"
        print(f"{ext}")
        with tempfile.NamedTemporaryFile(delete=False,suffix=ext) as temp:
            content=await file.read()
            temp.write(content)
            temp_path=temp.name     
        return StreamingResponse(Stream(temp_path,ext,filetype),media_type="text/event-stream")