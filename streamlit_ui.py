import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
import httpx, json, time

if "submitted" not in st.session_state:
    st.session_state.submitted=False

form=st.container()
stream=st.container()

with stream:
    output_placeholder = st.empty() 
 
def Request(file:UploadedFile, filetype:str):
    st.session_state.submitted=True
    files={
        "file":(
            file.name,
            file.getvalue(),
            file.type
        )
    }
    with httpx.stream("POST","http://127.0.0.1:8000/stream/",
                    params={"filetype":filetype},
                    files=files,
                    timeout=None) as response:
     stream_text=""
     for chunks in response.iter_text():
         stream_text+=chunks
         output_placeholder.write(f"{stream_text}")
        
        
with form:       
    if not st.session_state.submitted:
        st.title("Live Contract Risk & Obligation Scanner")
        st.subheader("Upload File for Scanning")
        uploaded=st.file_uploader(
            "Upload File",
            type=["pdf","txt","docx"],
            )
        filetype=st.radio("FILE TYPE",options=["text-pdf","image-pdf","text-file"],index=None)
        if filetype and uploaded:
            st.write(f" Done type:{filetype}")
        
        st.button("CHECK",on_click=Request, args=(uploaded,filetype))
 
    


    

    




