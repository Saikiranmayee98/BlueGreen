import os

def generate_local_summary(folder_path):
    summary = []

    # List all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Process each file and generate a summary
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Process content or use it as needed for summary
            # You can add more processing or generate a summary using the content
            summary.append(f"Summary for {file_name}:\n{content[:100]}...\n")

    return summary

if __name__ == "__main__":
    folder_path = r"C:\Users\s.sai.kiranmayee\Downloads\bluegreen"
    summaries = generate_local_summary(folder_path)

    # Print or use the summaries as needed
    for summary in summaries:
        print(summary)
