from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from pydantic import SecretStr
from dotenv import load_dotenv
import os
load_dotenv()
api=os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=SecretStr(api) if api is not None else None,
    temperature=0.1
)


prompt='''
Act like an experienced Lawyer, Analyse the following Data and List down Risks in the following Document.
Data:{data}
'''

llm_prompt=PromptTemplate(template=prompt, input_variables=["data"])

output_parser=StrOutputParser()

chain=(
    llm_prompt
    |llm
    |output_parser
)