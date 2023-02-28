import requests
import json

def get_bgp_routing_info(asn):
    url = f"https://api.bgpview.io/asn/{asn}/prefixes"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    return data

def print_current_routing_info(prefixes):
    print("Current routing information:\n", prefixes)

if __name__ == '__main__':
    asn = input("Enter a BGP ASN: ")
    data = get_bgp_routing_info(asn)
    if 'data' in data and 'ipv4_prefixes' in data['data']:
        prefixes = data['data']['ipv4_prefixes']
        print_current_routing_info(prefixes)
    else:
        print("No routing information available for this ASN.")
