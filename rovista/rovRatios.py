import requests
import json

def rov_ratios(date):
    # Build URL
    url = 'https://api.rovista.netsecurelab.org/rovista/api/ROV-adoption-ratios'
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
        if item['date'] == date:
            print(item)


#test code
inputDate = input("Input an date like 2024-04-01:")
rov_ratios(inputDate)