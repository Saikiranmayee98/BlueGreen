import openai
import graphviz

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

            # Create a Graphviz diagram
            dot = graphviz.Digraph(comment='Generated Summary')
            dot.node('A', 'Input Text')
            dot.node('B', 'Generated Summary')
            dot.edge('A', 'B', label='Summary Generation')

            # Save the diagram as an image
            dot.render('generated_summary_diagram', format='png', cleanup=True)

            return generated_summary

    except Exception as e:
        import traceback
        traceback.print_exc()

file_path = r"C:\Users\s.sai.kiranmayee\Downloads\bluegreen"
result = generate_summary_with_openai(file_path)
print(result)
