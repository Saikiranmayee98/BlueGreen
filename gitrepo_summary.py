import openai
import requests
import certifi
import os

# Set your OpenAI API token, base URL, and model
openai.api_key = '27940702532b4623b2c59a296bfe484b'
openai.api_base = 'https://devopsvalidation.openai.azure.com/'
openai.api_type = 'azure'
openai.api_version = '2023-09-15-preview'

model = 'devops'
file_path = r"C:\Users\s.sai.kiranmayee\Downloads\bluegreen" 
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
response = openai.Completion.create(
    engine=model,
    prompt=f"Generate Summary from {content}",  
    max_tokens=150,
    temperature=0.5,
)
var = response['choices'][0]['text']
print(var)


    


   
    
   
    
    