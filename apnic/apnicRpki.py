import csv
import requests



def country_Code(region):
    # open csv file
    with open('data/apnic.csv', mode='r') as file:

        # creat csv reader
        csvReader = csv.reader(file, delimiter='\t')
        
        # read the header from CSV
        headers = next(csvReader)

        # output country code
        for row in csvReader:
            if region == row[1]:
                return(row[0])
            elif region in row[1]:
                return(row[0])
            

def get_rpki(date, cn):
    cc = country_Code(cn)

    url = "https://stats.labs.apnic.net/cgi-bin/json-table.pl?x=" + cc
    try:
        response = requests.get(url)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print("Error fetching JSON:", e)
        return None

    data =  response.json()
    value = {}
    for item in data['data']:
        if item['date'] == date:
            value = item

    if value == {}:
        value = {"data not found": "check the input please."}

    return(value)



'''
print(get_rpki('2024-04-01', 'DE'))
'''

'''
print(country_Code('Europe'))
print(country_Code('Northern Europe'))
print(country_Code('Afghanistan'))
'''

'''
# input a date
inputDate = input("input a date like YYY-MM-DD:")

# input an IP address
inputRegion = input("input a region name like Germany or Asia:")

data = get_rpki(inputDate, country_Code(inputRegion))

for key, value in data.items():
    print(key + ": " + str(value))

'''
