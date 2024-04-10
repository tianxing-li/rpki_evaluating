import json


def asn_ripe():
    # 定义JSON文件路径
    json_file_path = "apnic.output.json"

    # 打开并读取JSON文件
    with open(json_file_path, "r") as file:
        data = json.load(file)

    print(data)


asn_ripe()