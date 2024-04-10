def find_childAS(file_path, asn):
    prefix = asn+"|"
    suffix = "|-1|bgp"
    # childlist = ""
    childlist = []
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if line.strip().startswith(prefix) and line.strip().endswith(suffix):
                    # print(f"In {line_number} find begins with '{prefix}' and ends with '{suffix}' :")
                    # print(line)
                    # childlist = childlist + line[len(prefix):-len(suffix)-1] + ", "
                    childlist.append(line[len(prefix):-len(suffix)-1])
            # print(f"Not found begins with '{prefix}' and ends with '{suffix}'")
    except FileNotFoundError:
        print("file not found")
    return childlist

def find_parentAS(file_path, asn):
    suffix = "|" + asn + "|-1|bgp"
    # parentlist = ""
    parentlist = []
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if line.strip().endswith(suffix):
                    # print(f"在第 {line_number} 行找到以 以 '{suffix}' 结尾的行：")
                    # print(line)
                    # parentlist = parentlist + line
                    parentlist.append(line[:-len(suffix)-1])
            # print(f"Not found ends with '{suffix}'")
    except FileNotFoundError:
        print("file not found")
    return parentlist

def find_peerAS(file_path, asn):
    prefix = asn+"|"
    suffix = "|0|bgp"
    suffixEnd = "|" + asn + "|0|bgp"
    p2plist = []
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if line.strip().startswith(prefix) and line.strip().endswith(suffix):
                    # print(f"In {line_number} find begins with '{prefix}' and ends with '{suffix}' :")
                    # print(line)
                    p2plist.append(line[len(prefix):-len(suffix)-1])
                elif line.strip().endswith(suffixEnd):
                    p2plist.append(line[:-len(suffixEnd)-1])
            # print(f"Not found begins with '{prefix}' and ends with '{suffix}'")
    except FileNotFoundError:
        print("file not found")
    return p2plist


# test code
asn = input("Input an ASN:")
date = "20240301"
file_path = date+".as-rel2.txt"


childas = find_childAS(file_path, asn)
parentas = find_parentAS(file_path, asn)
p2pas = find_peerAS(file_path, asn)

print("child list")
print(childas)
print("parent list")
print(parentas)
print("p2p list")
print(p2pas)