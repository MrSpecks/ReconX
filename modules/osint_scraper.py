import requests
import tweepy
from bs4 import BeautifulSoup

# Authenticate with the Twitter API
#def twitter_authenticate(api_key, api_secret, access_token, access_token_secret):
#    """Authenticate with the Twitter API."""
#    auth = tweepy.OAuthHandler(api_key, api_secret)
#    auth.set_access_token(access_token, access_token_secret)
    
#    api = tweepy.API(auth, wait_on_rate_limit=True)
#    return api

#def get_twitter_profile(api, username):
 #   """Retrieve Twitter profile information."""
 #   try:
  #      user = api.get_user(screen_name=username)
        
        # Fetch basic profile information
#        profile_info = {
#            "username": user.screen_name,
#            "name": user.name,
#            "bio": user.description,
#            "followers_count": user.followers_count,
#            "following_count": user.friends_count,
#            "tweets_count": user.statuses_count,
#            "profile_image_url": user.profile_image_url_https,
#            "created_at": user.created_at,
#        }
        
        # Return the profile information as a dictionary
#        return profile_info
#    except tweepy.TweepError as e:
#        return f"Error: {e}"

#def search_twitter_profiles(api, query, num_results=5):
#    """Search for Twitter profiles based on a query."""
#    try:
#        # Search Twitter for profiles related to the query
 #       users = tweepy.Cursor(api.search_users, q=query, count=num_results).items(num_results)
#        
#        profiles = []
#        for user in users:
#            profiles.append({
#                "username": user.screen_name,
#                "name": user.name,
#                "bio": user.description,
#                "followers_count": user.followers_count,
#                "profile_image_url": user.profile_image_url_https
#            })
#        return profiles
#    except tweepy.TweepError as e:
#        return f"Error: {e}"

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