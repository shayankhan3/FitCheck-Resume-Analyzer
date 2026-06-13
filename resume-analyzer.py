import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pypdf import PdfReader
from dotenv import load_dotenv


load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=os.getenv("GROQ_API_KEY"))

st.title("RESUME ANALYZER")
st.caption("upload you resume , AI analyze ")

upload_file=st.file_uploader("Upload your pdf",type="pdf")

if upload_file:
    reader=PdfReader(upload_file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
 

    st.success("Resume read completly")

    job_title=st.text_input("Enter job title")
    if job_title:
        if st.button("start analyzing"):
            with st.spinner("Ai is analyzing......."):

                prompt=ChatPromptTemplate.from_template("""
                Tum ek expert HR consultant ho. Resume analyze karo:
                
                Resume:
                {resume_text}
                
                Job Title: {job_title}
                
                Batao:
                1. Strengths
                2. Weaknesses
                3. Improvements
                4. Score (10/10)
                5. Job Match
                English mein jawab do.
                """)
                
                chain = prompt | llm | StrOutputParser()

                response=chain.invoke({
                    "resume_text":text,
                    "job_title":job_title

                })
                st.write('## Analyze')
                st.write(response)
                
                
                
