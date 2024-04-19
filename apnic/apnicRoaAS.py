import requests
            
def caculate_data(data, date, asn):
    ras_v4_robjs = 0
    ras_v4_addrs = 0
    ras_v4_val_robjs = 0
    ras_v4_val_addrs = 0
    ras_v4_inv_robjs = 0
    ras_v4_inv_addrs = 0
    ras_v4_unk_robjs = 0
    ras_v4_unk_addrs = 0

    ras_v6_robjs = 0
    ras_v6_addrs = 0
    ras_v6_val_robjs = 0
    ras_v6_val_addrs = 0
    ras_v6_inv_robjs = 0
    ras_v6_inv_addrs = 0
    ras_v6_unk_robjs = 0
    ras_v6_unk_addrs = 0

    for item in data:
        ras_v4_robjs += int(item['ras_v4_robjs'])
        ras_v4_addrs += int(item['ras_v4_addrs'])
        ras_v4_val_robjs += int(item['ras_v4_val_robjs'])
        ras_v4_val_addrs += int(item['ras_v4_val_addrs'])
        ras_v4_inv_robjs += int(item['ras_v4_inv_robjs'])
        ras_v4_inv_addrs += int(item['ras_v4_inv_addrs'])
        ras_v4_unk_robjs += int(item['ras_v4_unk_robjs'])
        ras_v4_unk_addrs += int(item['ras_v4_unk_addrs'])

        ras_v6_robjs += int(item['ras_v6_robjs'])
        ras_v6_addrs += int(item['ras_v6_addrs'])
        ras_v6_val_robjs += int(item['ras_v6_val_robjs'])
        ras_v6_val_addrs += int(item['ras_v6_val_addrs'])
        ras_v6_inv_robjs += int(item['ras_v6_inv_robjs'])
        ras_v6_inv_addrs += int(item['ras_v6_inv_addrs'])
        ras_v6_unk_robjs += int(item['ras_v6_unk_robjs'])
        ras_v6_unk_addrs += int(item['ras_v6_unk_addrs'])

    return {'date': date, 'asn': asn, 'ras_v4_robjs': ras_v4_robjs, 'ras_v4_addrs': ras_v4_addrs,\
     'ras_v4_val_robjs': ras_v4_val_robjs, 'ras_v4_val_addrs': ras_v4_val_addrs,\
      'ras_v4_inv_robjs': ras_v4_inv_robjs, 'ras_v4_inv_addrs': ras_v4_inv_addrs,\
       'ras_v4_unk_robjs': ras_v4_unk_robjs, 'ras_v4_unk_addrs': ras_v4_unk_addrs,\
        'ras_v6_robjs': ras_v6_robjs, 'ras_v6_addrs': ras_v6_addrs,\
         'ras_v6_val_robjs': ras_v6_val_robjs,'ras_v6_val_addrs': ras_v6_val_addrs,\
          'ras_v6_inv_robjs': ras_v6_inv_robjs, 'ras_v6_inv_addrs': ras_v6_inv_addrs,\
           'ras_v6_unk_robjs': ras_v6_unk_robjs, 'ras_v6_unk_addrs': ras_v6_unk_addrs}


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
        return([{"data not found": "check the input please."}],\
         {"data not found": "maybe there is no data for this AS"})

    data_sum = caculate_data(value, date, asn)

    return(data_sum)

    # return(value, data_sum)


'''
# input a date
inputDate = input("input a date like YYY-MM-DD:")

# input an IP address
inputASN = input("input a AS number like 42:")

data, datasum = get_roa_as(inputDate, inputASN)

for item in data:
    print(item)

print(datasum)
'''