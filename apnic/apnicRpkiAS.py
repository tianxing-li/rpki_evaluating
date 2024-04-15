import requests
import json


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # check response status
        return response.text       # get origin text
    except requests.exceptions.RequestException as e:
        return("Error fetching JSON:", e)

def save_data_to_file(json_text, filename):
    try:
        with open(filename, 'w') as f:
            f.write(json_text)
        print("JSON data saved to", filename)
    except IOError as e:
        print("Error saving JSON to file:", e)


def find_text_in_json(filename, text):
    try:
        with open(filename, 'r') as f:
            # read file line by line
            lines = f.readlines()
            # check if the line contain the data
            for i, line in enumerate(lines, start=1):
                if text in line:
                    return({line.strip()})
    except IOError as e:
        print("Error reading file:", e)

def get_rpki_as(date, asn):
    url = "https://stats.labs.apnic.net/cgi-bin/rpki-json-table.pl?x=" + asn
    rawData = fetch_data(url)
    if rawData:
        save_data_to_file(rawData, asn + "rpki_data.json")
    else:
        return("Failed to fetch data.")


    data = find_text_in_json(asn + "rpki_data.json", '"date": "' + date + '"')
    
    # data = json.loads(response.text.replace("'", '"'), strict=False)
    # print(data.type())

    '''
    value = {}
    for item in data['data']:
        if item['date'] == date:
            value = item
            # print(item)

    if value == {}:
        value = {"data not found": "check the input please."}
    '''

    return(data)



# input a date
inputDate = input("input a date like YYY-MM-DD:")

# input an IP address
inputASN = input("input a AS number like 199140:")

record = get_rpki_as(inputDate, inputASN)

print(record)
