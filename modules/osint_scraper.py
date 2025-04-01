import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=5):
    """Performs a simple Google search and extracts links."""
    headers = {"User-Agent": "Mozilla/5.0"}
    search_url = f"https://www.google.com/search?q={query}"
    
    try:
        response = requests.get(search_url, headers=headers)
        
        # Debug: Check if the request was successful
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            results = []
            for link in soup.select("a"):
                href = link.get("href", "")
                if "url?q=" in href and "webcache" not in href:
                    results.append(href.split("url?q=")[1].split("&")[0])
                    if len(results) >= num_results:
                        break
            print(f"Results found: {len(results)}") # Debug: Print number of results
            return results
        else:
            return f"Error: Unable to fetch Google results (Status {response.status_code})"
    except Exception as e:
        return f"Error: {e}"

def github_search(username):
    """Fetches public repositories from a GitHub user profile."""
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()
            return [repo["html_url"] for repo in repos]
        else:
            return f"Error: Unable to fetch GitHub profile (Status {response.status_code})"
    except Exception as e:
        return f"Error: {e}"