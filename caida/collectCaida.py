import requests
import bz2
import os


def caidadata_download(date):
    date = date.replace("-", "")[:6]
    # data download link
    url = "https://publicdata.caida.org/datasets/as-relationships/serial-2/"+ date +"01.as-rel2.txt.bz2"
    
    # print(url)

    # download data link
    download_path = "data/" + date + "01.as-rel2.txt.bz2"

    # data download
    response = requests.get(url)
    if response.status_code == 200:
        with open(download_path, 'wb') as f:
            f.write(response.content)
        print("Download Successed")
    else:
        print("Download Failed")

    # decompress data set
    output_path = "data/" + date + "01.as-rel2.txt"
    with open(download_path, 'rb') as f:
        compressed_data = f.read()

    with open(output_path, 'wb') as f:
        decompressed_data = bz2.decompress(compressed_data)
        f.write(decompressed_data)

    print("Decompressed is Done")

    # delete compressed data set
    os.remove(download_path)
    print("Compressed Data is Deleted")

'''
#test code
acdate = input("please input a date in yyyymmdd format：")
caidadata_download(acdate)
'''