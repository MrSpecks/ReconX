import argparse
from modules.domain_recon import get_whois_info, get_dns_records

def main():
    parser = argparse.ArgumentParser(description="ReconX - Automated Reconnaissance Tool")
    parser.add_argument("-d", "--domain", help="Domain to perform reconnaissance on")
    
    args = parser.parse_args()

    if args.domain:
        print(f"\n[+] Fetching WHOIS info for {args.domain}...")
        whois_data = get_whois_info(args.domain)
        for key, value in whois_data.items():
            print(f"{key}: {value}")

        print(f"\n[+] Fetching DNS records for {args.domain}...")
        dns_data = get_dns_records(args.domain)
        for record_type, values in dns_data.items():
            print(f"{record_type}: {values}")

if __name__ == "__main__":
    main()