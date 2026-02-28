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
You are an experienced contract risk analyst.

Extract only NEW risks and obligations found in this portion of the contract.
Be concise.
Do not repeat headings.
Return bullet points only.
Do not restate category titles unless necessary.

Document Chunk:
{data}

'''


prompt2='''
Act like an experienced Contract reviewer, categorizer the followin risks into:
1. Financial Risks and Obligations
2. Legal and Compliance Obligations
3. Operational Risks and Performance
4. Security and Data Risks
5. Renewal and Strategic Risks
6. Vendor/Counterparty Specifics
Generate a summery and conclusion for it.
Risks:{risk}
'''





llm_prompt=PromptTemplate(template=prompt, input_variables=["data"])
llm_prompt2=PromptTemplate(template=prompt2, input_variables=["risk"])

output_parser=StrOutputParser()

chain=(
    llm_prompt
    |llm
    |output_parser
)


chain2=(
    llm_prompt2
    |llm
    |output_parser
)