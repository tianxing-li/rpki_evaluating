import requests
            

def get_roa_as(date, asn):
    url = "https://stats.labs.apnic.net/roa/AS" + asn + "?hf=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print("Error fetching JSON:", e)
        return None

    data =  response.json()
    value = []
    for item in data['data']:
        if item['ras_dt'] == date:
            value.append(item)

    if value == []:
        value = [{"data not found": "check the input please."}]

    return(value)



# input a date
inputDate = input("input a date like YYY-MM-DD:")

# input an IP address
inputASN = input("input a AS number like 42:")

data = get_roa_as(inputDate, inputASN)

for item in data:
    print(item)
