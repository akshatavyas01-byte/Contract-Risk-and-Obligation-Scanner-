from fastapi import FastAPI,UploadFile, File, Query
from fastapi.responses import StreamingResponse
import tempfile
from functions import document_loading 
import  time, os
app=FastAPI()

def Stream(doc):
    if doc:
        yield f"AI: HERE"
        time.sleep(3)
    for d in doc:
      yield d.page_content
    

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
        doct=await document_loading(temp_path, filetype, ext)
    else:  
        doct=None 
    return StreamingResponse(Stream(doct),media_type="text/event-stream")