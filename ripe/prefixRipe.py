import json

def pre_ripe(tal, pre):
    # file path
    json_file_path = "data/" + tal + ".output.json"
    asn = []

    # read data
    with open(json_file_path, "r") as file:
        data = json.load(file)

    for item in data["roas"]:
    	if item["prefix"] == pre:
    		asn.append(item)

    return asn


inputPrefix = input("Input an Prefix like 45.6.214.0/24:")
asnCollection = []
for tal in ["afrinic", "lacnic", "apnic", "arin", "ripencc"]:
    asnCollection = asnCollection + pre_ripe(tal, inputPrefix)


for item in asnCollection:
	print(item)