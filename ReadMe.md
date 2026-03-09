# Risks and Obligtion Scanner

## 1. Overview

``AI-powered legal document analyzer that extracts risks and obligations from contracts using LLM orchestration.``

## 2. Problem Statement
Legal Contracts are lengthy and complex. Clients usually sign without clearly identifying:
1. Financial Risks and Obligations
2. Legal and Compliance Obligations
3. Operational Risks and Performance
4. Security and Data Risks
5. Renewal and Strategic Risks
6. Vendor/Counterparty Specifics

Manual review is expensive and slow.

## 3. Solution Approach
This project uses LLM based pipeline to analyze uploaded documents into steps:
 1. Document is split in chunks to handle large text.
 2. Each chunk is analysed to extract risks and obligations.
 3. Extracted risks are then summarized and categorized.
 4. Results are streamed to the UI in real time.

The focus of this project was building a working streaming system with document processing.

## 4. Key Features
 - Upload PDF, DOCX, or text files
 - Chunk-based document processing
 - Real-time streaming of LLM responses
 - Categorized risk summary
 - Simple session-based handling

## 5. System Architecture

- Frontend - Streamlit
- Backend - FastAPI
- LLM - GROQ (LLaMA 3.3 70B )
- LLM-Orchestration - LangChain
- Document Parsing - PDF/DOCX loaders
- Streaming - HTTPX streaming
- Session handling - In-memory session store`

## 6. Tech Stack

- **Language:** Python  
- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **LLM Orchestration:** LangChain  
- **Model Provider:** Groq (LLaMA 3.3 70B)  
- **Streaming:** HTTPX  
- **Environment Management:** python-dotenv  

## 7. How It Works (Execution Flow)

1. User Upload:
User uploadds a legal document and selects its type.

2. Docuemnt loading:
The backend reads and extracts the text using appropriate (PDF/DOCX/TXT) loader or pdf2image(OCR) then loading.

3. Chunking:
The extracted text is spilt using CharacterTextSpiltter to stay within LLM token limit.

4. Prompt Injection:
- Each chunk is inserted into a structured prompt for risk analysis. 
- The Extracted risks of each chunk is instered into a structured prompt for summarization and categorization of the risks.

5. LLM Processing:
- The model analysis risks from each chunk.
- The model categorizes the risks and generates a summary for the document.

6. Streaming the Response:
- The backend streams the generated risks, categorization of risks and summary to the frontend in real time.

7. UI Persistance:
- The streamed output remains visible until user proceeds further.


## 8. Example Input & Output
<!-- INPUT- DOCUMENT SELECTION + DOCUMENT TYPE SELECTION

OUTPUT- RISKS --> 
### 1. Docker run:
![Alt Text](images\docker_run.png)

### 2. Streamlit UI:
![Alt Text](images\streamlit_ui.png)

### 3. Upload document:
![Alt Text](images\upload_document.png)

### 4. Streamed Risk:
![Alt Text](images\risks_streamed.png)

### 5. Video Demo:
[![Watch Demo](images\streamlit_ui.png)](https://www.youtube.com/watch?v=GqmT0u1-EBc)


## 9. Installation & Setup
1. Clone the Repository:
```python
git clone https://github.com/your-username/risk-analyser.git
cd risk-analyser
```
2. Create Virtual Environment
```python
python -m venv .venv
```
Activate it:
Windows vscode terminal:
```python
.venv\Scripts\Activate.ps1
```
3. Install Dependencies
```python
pip install -r requirements.txt
```
4. Add Environment Variables
Create a .env file and add:
```python
GROQ_API_KEY=your_api_key_here
```

## 10. Usage
1. Start the backend server:
```python
uvicorn main:app --reload
```
2. Run the streamlit frontend:
```python
streamlit run streamlit_ui.py
```
3. Open the browser and:
 - Upload a legal document (PDF/DOCX/TXT)
 - Select the document type
 - Click submit
 - View streamed risk analysis in real-time

4. The generated risks remain visible until the user uploads a new document.

### With DOCKER
1. Build the docker image:
```python
docker build -t risk_analyser .
``` 
2. Run the container:
```python
docker run -p 8000:8000 risk_analyser 
```
3. Open the application in your browser and upload a document.

## 11. Project Structure

     project/
            |── src/
            |   |── main.py
            |   |── LLM.py
            |   |── streamlit_ui.py
            |   |── functions.py
            |
            |── images/
            |
            |── Test/
            |   |── Legal-Services-Agreement.pdf
            |
            |── .env
            |
            |── dockerfile
            |── start.sh
            |
            |── requirements.txt
            |
            └── ReadMe.md

## 12. Limitations
- Very large documents (>200MB) are not supported
- Risk reports are not persisted
- No authentication system
- Some duplicate risks may appear due to chunk overlap

## 13. Future Improvements
- Token-aware chunking
- Risk deduplication logic
- Database integration for storing reports
- Contract comparison feature
- Structured JSON export

## 14. License
This project is licensed under the MIT License.

## 15. Author
**Akshata Vyas**  
GitHub: [akshatavyas01-byte](https://github.com/akshatavyas01-byte)