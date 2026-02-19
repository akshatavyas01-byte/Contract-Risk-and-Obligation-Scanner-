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
Act like an experienced Lawyer, Analyse the following Document Data check it for the following risks and others you can discover:
1. Financial Risks and Obligations
2. Legal and Compliance Obligations
3. Operational Risks and Performance
4. Security and Data Risks
5. Renewal and Strategic Risks
6. Vendor/Counterparty Specifics

Document Data:{data}
'''

llm_prompt=PromptTemplate(template=prompt, input_variables=["data"])

output_parser=StrOutputParser()

chain=(
    llm_prompt
    |llm
    |output_parser
)