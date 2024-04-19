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

def world_ROV_Score(inputType, cn):
    try:
        dataType = bool(inputType)
    except ValueError:
        print("Invalid Input, make sure input True or False")

    cc = countries(cn).lower()

    # Build URL
    if type == True:
        url = 'https://api.rovista.netsecurelab.org/rovista/api/world-rov-scores?type=cone-size'
    else:
        url = 'https://api.rovista.netsecurelab.org/rovista/api/world-rov-scores?type=address-space'

    # Request GET
    try:
        response = requests.get(url)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print("Error fetching JSON:", e)
        return None

    # Check Response Status
    if response.status_code == 200:
        # Process Request Data
        data = response.json()
    else:
        return ("Requests Failed:", response.status_code)


    for item in data:
        if item['countryCode'] == cc:
            return(item)




'''
# test code
inputType = input("Chooes data type, False is adress space, True is cone size:")

try:
    dataType = bool(inputType)
    for item in world_ROV_Score(dataType):
        print(item)
except ValueError:
    print("Invalid Input, make sure input True or False")

'''
