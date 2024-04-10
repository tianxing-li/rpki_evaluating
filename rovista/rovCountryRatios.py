import requests
import json

def countries(countryName):
    # Build URL
    url = 'https://api.rovista.netsecurelab.org/rovista/api/countries'
    # Request GET
    response = requests.get(url)
    countryCode = {}


    # Check Response Status
    if response.status_code == 200:
        # Process Request Data
        countryCode = response.json()
    else:
        print("Requests Failed:", response.status_code)

    for item in countryCode:
        if item['country'] == countryName:
            return item['countryCode']


def rov_country_ratios(countryNameISO, date):
    # Build URL
    url = 'https://api.rovista.netsecurelab.org/rovista/api/ROV-country-adoption-ratios?country-iso=' + countryNameISO
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
        if item['countryDateKey']['recordDate'] == date:
            print(item)


#test code
inputCN = input("Input an country name like Germany:")
inputDate = input("Input an date like 2024-04-01:")
cn = countries(inputCN)
rov_country_ratios(cn, inputDate)