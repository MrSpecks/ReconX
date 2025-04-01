import argparse
import requests
from bs4 import BeautifulSoup
from modules.osint_scraper import google_search, github_search
from modules.domain_recon import get_whois_info, get_dns_records
#from modules.osint_scraper import twitter_authenticate, get_twitter_profile, search_twitter_profiles

def main():
    parser = argparse.ArgumentParser(description="ReconX - Automated Reconnaissance Tool")
    parser.add_argument("-d", "--domain", help="Perform domain reconnaissance")
    parser.add_argument("-g", "--google", help="Search Google for a keyword")
    parser.add_argument("-gh", "--github", help="Get GitHub repos for a user")
     # Add Twitter-related arguments
    #parser.add_argument('-t', '--twitter', help="Twitter username to gather footprint data.")
    #parser.add_argument('-q', '--query', help="Search query for Twitter footprint search.")

    args = parser.parse_args()  # <-- This line defines 'args'

     # Twitter API keys (replace with your actual keys)
    #api_key = "C7AQfdbmbu34XLGFZyNx0WSpa"
    #api_secret = "E4QXXO2sHetnWlUKJBDb2SZ3rrKTmMnlXKu5vdcimo4xN6nUIB"
    #access_token = "1907169515596918784-Sca1DYd9svm4M5TJtZeicPVWigz5TG"
    #access_token_secret = "6Z9acH9x4lxiUszSRvLeqwrYJOLUXuLADeSnOjjPdPdmp"
   
    # Authenticate with Twitter
    #api = twitter_authenticate(api_key, api_secret, access_token, access_token_secret)
 
    # Fetch Twitter profile info if username is provided
    #if args.twitter:
     #   profile = get_twitter_profile(api, args.twitter)
    #    print(f"Twitter Profile Info: {profile}")
   
    # Search for Twitter profiles based on query
    #if args.query:
     #   profiles = search_twitter_profiles(api, args.query)
     #   print(f"Found {len(profiles)} profiles related to '{args.query}':")
     #   for profile in profiles:
     #       print(profile)

    if args.domain:
        print(f"\n[+] Fetching WHOIS info for {args.domain}...")
        whois_data = get_whois_info(args.domain)
        for key, value in whois_data.items():
            print(f"{key}: {value}")

        print(f"\n[+] Fetching DNS records for {args.domain}...")
        dns_data = get_dns_records(args.domain)
        for record_type, values in dns_data.items():
            print(f"{record_type}: {values}")

    if args.google:
        print(f"\n[+] Searching Google for '{args.google}'...")
        results = google_search(args.google)
        for link in results:
            print(link)

    if args.github:
        print(f"\n[+] Fetching GitHub repos for user '{args.github}'...")
        repos = github_search(args.github)
        for repo in repos:
            print(repo)

if __name__ == "__main__":
    main()

