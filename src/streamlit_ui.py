import streamlit as st
import httpx

if "submitted" not in st.session_state:
    st.session_state.submitted=False

if "processing" not in st.session_state:
    st.session_state.processing=False

if "output" not in st.session_state:
    st.session_state.output=""

if st.session_state.processing:
    stream_text=""
    output_placeholder=st.empty()
    file=st.session_state.uploaded
    filetype=st.session_state.file_type
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
   
     for chunks in response.iter_text():
         stream_text+=chunks 
         output_placeholder.write(f"{stream_text}")
    
    st.session_state.output=stream_text
    st.session_state.processing=False
    st.rerun()
    

              
if not st.session_state.submitted:
    st.title("Live Contract Risk & Obligation Scanner")
    st.subheader("Upload File for Scanning")
    uploaded=st.file_uploader(
            "Upload File",
            type=["pdf","txt","docx"],
            )
    filetype=st.radio("FILE TYPE",options=["text-pdf","image-pdf","text-file"],index=None)
    
    if st.button("CHECK") and uploaded and filetype:
        st.session_state.uploaded=uploaded
        st.session_state.file_type=filetype
        st.session_state.submitted=True
        st.session_state.processing=True
        st.rerun()

def Reload():
    keys=["output",'processing','submitted','uploaded','file_type']
    for key in keys:
        if key in st.session_state:
            del st.session_state[key]
    

if st.session_state.output:
    st.write(st.session_state.output)
    st.button("Next Document",on_click=Reload)


        
 
    


    

    




