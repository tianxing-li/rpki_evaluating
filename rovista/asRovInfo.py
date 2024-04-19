import requests
import json

def as_rov_info(asn):
    # Build URL
    url = 'https://api.rovista.netsecurelab.org/rovista/api/overview?offset=0&count=10000&sortBy=asn&sortOrder=asc&searchBy=ASN&search=' + asn
    # Request GET
    response = requests.get(url)

    # Check Response Status
    if response.status_code == 200:
        # Process Request Data
        data = response.json()
    else:
        print("Requests Failed:", response.status_code)

    return(data)

'''
    asn = int(asn)

    for item in data['data']:
        if item['asn'] == asn:
            print("ASN:", item['asn'])
            print("Rank:", item['rank'])
            print("Organization:", item['organization'])
            print("Country:", item['country'])
            print("Country ISO:", item['countryIso'])
            print("Ratio:", item['ratio'])
            print("Last Updated Date:", item['lastUpdatedDate'])
            print("Cone Size:", item['coneSize'])
            print("Number of Addresses:", item['numberOfAddresses'])
            break
    else:
        print("ASN not found:", asn)
'''

'''
inputASN = input("Input an ASN:")
as_rov_info(inputASN)
'''