from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
model= ChatOpenAI(model='gpt-3.5-turbo')
result= model.invoke('Tell me in 2 lines how to remain happy')
print("Full result")
print(result)
print("content only")
print(result.content)