import argparse
import requests
from bs4 import BeautifulSoup
from modules.osint_scraper import google_search, github_search
from modules.domain_recon import get_whois_info, get_dns_records

def main():
    parser = argparse.ArgumentParser(description="ReconX - Automated Reconnaissance Tool")
    parser.add_argument("-d", "--domain", help="Perform domain reconnaissance")
    parser.add_argument("-g", "--google", help="Search Google for a keyword")
    parser.add_argument("-gh", "--github", help="Get GitHub repos for a user")

    args = parser.parse_args()  # <-- This line defines 'args'

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

