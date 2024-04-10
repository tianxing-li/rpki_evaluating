import requests

def world_ROV_Score(type):
    # Build URL
    if type == True:
        url = 'https://api.rovista.netsecurelab.org/rovista/api/world-rov-scores?type=cone-size'
    else:
        url = 'https://api.rovista.netsecurelab.org/rovista/api/world-rov-scores?type=address-space'

    # Request GET
    response = requests.get(url)

    # Check Response Status
    if response.status_code == 200:
        # Process Request Data
        data = response.json()
        return data
    else:
        return ("Requests Failed:", response.status_code)





# test code
inputType = input("Chooes data type, False is adress space, True is cone size:")

try:
    dataType = bool(inputType)
    for item in world_ROV_Score(dataType):
        print(item)
except ValueError:
    print("Invalid Input, make sure input True or False")


