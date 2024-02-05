import os

def generate_local_summary(folder_path):
    summaries = []

    # List all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Process each file and generate a summary
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Generate PlantUML code based on file content
            plantuml_code = f"""
            @startuml
            class File {{
                + name: String
                + size: int
            }}

            class Summary {{
                + data: String
                + visualize(): void
            }}

            File -- Summary : Contains
            @enduml
            """

            # Append PlantUML code and file summary to the result
            summaries.append(f"PlantUML Code for {file_name}:\n{plantuml_code}\n")
            summaries.append(f"Summary for {file_name}:\n{content[:100]}...\n")

            # Save the PlantUML code to a file (optional)
            plantuml_file_path = os.path.join(folder_path, f"{file_name}_plantuml.txt")
            with open(plantuml_file_path, 'w', encoding='utf-8') as plantuml_file:
                plantuml_file.write(plantuml_code)

    return summaries

if __name__ == "__main__":
    folder_path = r"C:\Users\s.sai.kiranmayee\Downloads\bluegreen"
    summaries = generate_local_summary(folder_path)

    # Print or use the summaries as needed
    for summary in summaries:
        print(summary)
