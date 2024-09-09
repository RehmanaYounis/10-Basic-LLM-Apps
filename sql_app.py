import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
import sqlite3
import streamlit as st
import import_ipynb
from langchain.prompts import ChatPromptTemplate
from LLM_Interaction_with_SQL import read_from_db

prompt= """
    You are an expert in translating English questions into SQL queries.
    Below are few examples how you will see question and how your answer should look like
    For example:
    Question: "How many entries of records are present?"
    SQL Query: SELECT COUNT(*) FROM STUDENT;
    Question: "Tell me all the students studying in Data Science class?"
    SQL Query: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
    Ensure that the generated SQL code is clear, without enclosing it in any backticks (```), 
    and avoid including the word "SQL" in the output. 
    
    Question : {question}
    """

Prompt_template = ChatPromptTemplate.from_template(prompt)

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

st.set_page_config(page_title="Database Agent")
st.header("App to Interact with Database")
question=st.text_input("Input: ", key="input")
formatted_prompt = prompt.format(question=question)
submit=st.button("Question")
if submit:
    query=model.invoke(formatted_prompt)
    print("LLM generated the following query:/n", query)
    response=read_from_db(query=query.content, db="students_records.db")
    st.subheader("Result from Database")
    for row in response:
        st.write(row)
        #st.header(row)
        
        
# formatted_prompt = prompt.format(question="show me all students")
# query=model.invoke(formatted_prompt)
# print("LLM generated the following query:\n", query.content)
# response=read_from_db(query=query.content, db="students_records.db")