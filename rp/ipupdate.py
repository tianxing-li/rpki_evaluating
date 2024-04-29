import sqlite3
import subprocess
import re

def get_whois_info(ip_address):
    try:
        # use Linux's whois command
        command = f"whois {ip_address}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # analysis whois output，get origin and country information
        origin = None
        country = None
        nic_hdl = None

        print(result)


        # check result
        if result.returncode == 0:
            whois_output = result.stdout

            # get origin and country information
            origin_match = re.search(r'origin:\s*(\S+)', whois_output, re.IGNORECASE)
            originas_match = re.search(r'OriginAS:\s*(\S+)', whois_output, re.IGNORECASE)
            aut_num = re.search(r'aut-num:\s*(\S+)', whois_output, re.IGNORECASE)
            country_match = re.search(r'country:\s*(\S+)', whois_output, re.IGNORECASE)
            nic_hdl_match = re.search(r'nic-hdl:\s*(\S+)', whois_output, re.IGNORECASE)

            if origin_match:
                origin = origin_match.group(1)
            elif originas_match:
                origin = originas_match.group(1)
            elif aut_num:
                origin = aut_num.group(1)
            if country_match:
                country = country_match.group(1)
            if nic_hdl_match:
                nic_hdl = nic_hdl_match.group(1)

        return origin, country, nic_hdl

    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None, None


def ipdbupdate():

    # connect to database
    db_path = '../data/whoisip.sqlite'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get the IP where the ASN not exist
    cursor.execute("SELECT ip FROM ip_info WHERE asn IS NULL")
    rows = cursor.fetchall()

    # make whois query
    for row in rows:
        ip = row[0]
        asn, country, nic_hdl = get_whois_info(ip)
        cursor.execute("UPDATE ip_info SET asn = ?, country = ?, nic_hdl = ? WHERE ip = ?", (asn, country, nic_hdl, ip))
        conn.commit()


    # close connection
    conn.close()
    


def main():
    ipdbupdate()

if __name__ == "__main__":
    main()