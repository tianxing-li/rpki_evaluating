import json

def asn_ripe(tal, asn):
    # file path
    json_file_path = "data/" + tal + ".output.json"
    prefix = []

    # read data
    with open(json_file_path, "r") as file:
        data = json.load(file)

    for item in data["roas"]:
    	if item["asn"] == asn:
    		prefix.append(item)

    return prefix

def asn_all(asn):
    data = []
    for tal in ["afrinic", "lacnic", "apnic", "arin", "ripencc"]:
        data += asn_ripe(tal, "AS" + asn)

    return(data)



'''
data = asn_all("42235")
for i in data:
    print(i)
'''


'''
inputASN = "AS" + input("Input an ASN like 42235:")
prefixCollection = []
for tal in ["afrinic", "lacnic", "apnic", "arin", "ripencc"]:
    prefixCollection = prefixCollection + asn_ripe(tal, inputASN)


for item in prefixCollection:
	print(item)
'''