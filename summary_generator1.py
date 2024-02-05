import requests

def generate_github_repo_summary(repo_url):
    # Parse the GitHub repository URL to extract username and repo name
    parts = repo_url.rstrip('/').split('/')
    username, repo_name = parts[-2], parts[-1]

    # Construct the API URL for the GitHub repository
    api_url = f"https://api.github.com/repos/{username}/{repo_name}"

    # Fetch repository information using GitHub API
    response = requests.get(api_url)
    repo_info = response.json()
    repo_name = repo_info.get('name', 'N/A')
    # owner_login = repo_info['owner'].get('login', 'N/A')
    # description = repo_info.get('description', 'No description available')
    # Fetch contents of the repository using GitHub API
    contents_url = f"{api_url}/contents"
    contents_response = requests.get(contents_url)
    contents_data = contents_response.json()

    # Process the repository information and contents as needed for summary
    summary = f"Summary for GitHub Repository: {repo_url}\n"
    summary += f"Repository Name: {repo_info['name']}\n"
    summary += f"Owner: {repo_info['owner']['login']}\n"
    summary += f"Description: {repo_info['description']}\n\n"

    summary += "Contents:\n"
    for content in contents_data:
        if content['type'] == 'file':
            summary += f"File: {content['name']}\n"
            # You can fetch and process the file content here if needed
            summary += "\n"

    return summary

if __name__ == "__main__":
    repo_url = "https://github.com/Saikiranmayee98/BlueGreen.git"
    repo_summary = generate_github_repo_summary(repo_url)
    print(repo_summary)
