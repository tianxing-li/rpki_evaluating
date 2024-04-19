import requests
import tarfile
import os
import lzma


def data_download(tal, date):

    # URL define
    url = "https://ftp.ripe.net/rpki/" + tal + ".tal/" + date + "/output.json.xz"
    # file path define
    file_path = "data/output.json.xz"
    # output path defin
    output_path = "data/" + tal + ".output.json"

    # data downloading
    # print("begin...")
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)
    # print("download successed")

    # decompressing
    # print("begin to decompress...")
    with lzma.open(file_path, "rb") as compressed_file:
        with open(output_path, "wb") as output_file:
            output_file.write(compressed_file.read())
    print(tal, " decompress done")

    # delete raw file
    os.remove(file_path)
    # print("downloaded file deleted")

def tal_loop(date):
    date = date.replace("-", "/")
    for tal in ["afrinic", "lacnic", "apnic", "arin", "ripencc"]:
        data_download(tal, date)


'''
inputDate = input("Input an date like 2024-04-01:")
date = inputDate.replace("-", "/")
for tal in ["afrinic", "lacnic", "apnic", "arin", "ripencc"]:
    data_download(tal, date)
'''