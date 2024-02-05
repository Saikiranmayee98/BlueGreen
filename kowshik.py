import openai
 
def generate_summary_with_openai(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
 
            openai.api_type = "azure"
            openai.api_base = "https://genwizard-adm-brownfield-switzerlandnorth.openai.azure.com/"
            openai.api_version = "2023-09-15-preview"
            openai.api_key = "117541d79dc04afd9dcbdf23311d6368"
           
            messages = [{'role': 'user', 'content': f"Summarize the following text:\n{content}"}]
           
            response = openai.ChatCompletion.create(
                engine="genwizard-adm-gpt4-32k",
                messages=messages,
                temperature=0,  # Adjust the temperature for creativity
                max_tokens=3000
            )
 
            generated_summary = response['choices'][0]['message']['content'].strip()
 
            return generated_summary
 
    except Exception as e:
        import traceback
        traceback.print_exc()
 
 
file_path = r"C:\Users\kowshik.bhasuru\OneDrive - Accenture\Documents\My Work professional\Python\genai\chunking file to be.txt"
result = generate_summary_with_openai(file_path)
print(result)