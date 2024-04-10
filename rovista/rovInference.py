import requests
import json

def rov_inference(asn, date):
    # Build URL
    url = 'https://api.rovista.netsecurelab.org/rovista/api/inference-results/' + asn + '?date=' + date
    # Request GET
    response = requests.get(url)
    data = {}


    # Check Response Status
    if response.status_code == 200:
        # Process Request Data
        data = response.json()
    else:
        print("Requests Failed:", response.status_code)


    asn = int(asn)

    for item in data:
        print(item)


inputASN = input("Input an ASN like 3356:")
inputDate = input("Input an Date like 2024-04-01:")
rov_inference(inputASN, inputDate)