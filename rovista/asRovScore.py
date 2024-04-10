import requests
import json

def rov_ratios(asn, date):
    # Build URL
    url = 'https://api.rovista.netsecurelab.org/rovista/api/AS-rov-scores/' + asn
    # Request GET
    response = requests.get(url)
    data = {}


    # Check Response Status
    if response.status_code == 200:
        # Process Request Data
        data = response.json()
    else:
        print("Requests Failed:", response.status_code)

    for item in data:
        if item['asnDateKey']['recordDate'] == date:
            print(item)


#test code
inputASN = input("Input an ASN like 3356:")
inputDate = input("Input an date like 2024-04-01:")
rov_ratios(inputASN, inputDate)