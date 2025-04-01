import whois
import dns.resolver

def get_whois_info(domain):
    """Fetch WHOIS information for a domain."""
    try:
        w = whois.whois(domain)
        return {
            "Domain": domain,
            "Registrar": w.registrar,
            "Creation Date": w.creation_date,
            "Expiration Date": w.expiration_date,
            "Nameservers": w.name_servers
        }
    except Exception as e:
        return {"Error": str(e)}

def get_dns_records(domain):
    """Retrieve DNS records (A, MX, NS)."""
    records = {}
    try:
        records["A"] = [str(ip) for ip in dns.resolver.resolve(domain, "A")]
    except:
        records["A"] = "No A records found"

    try:
        records["MX"] = [str(mx) for mx in dns.resolver.resolve(domain, "MX")]
    except:
        records["MX"] = "No MX records found"

    try:
        records["NS"] = [str(ns) for ns in dns.resolver.resolve(domain, "NS")]
    except:
        records["NS"] = "No NS records found"

    return records