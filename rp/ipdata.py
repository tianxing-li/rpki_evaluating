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


        # check result
        if result.returncode == 0:
            whois_output = result.stdout

            # get origin and country information
            origin_match = re.search(r'origin:\s*(\S+)', whois_output, re.IGNORECASE)
            originas_match = re.search(r'OriginAS:\s*(\S+)', whois_output, re.IGNORECASE)
            country_match = re.search(r'country:\s*(\S+)', whois_output, re.IGNORECASE)
            nic_hdl_match = re.search(r'nic-hdl:\s*(\S+)', whois_output, re.IGNORECASE)

            if origin_match:
                origin = origin_match.group(1)
            elif originas_match:
                origin = originas_match.group(1)
            if country_match:
                country = country_match.group(1)
            if nic_hdl_match:
                nic_hdl = nic_hdl_match.group(1)

        return origin, country, nic_hdl

    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None, None


def ipdb():
    # connect to the RP database
    source_db_path = '../data/krill1-log.sqlite'
    conn_source = sqlite3.connect(source_db_path)
    c_source = conn_source.cursor()

    # connect to 
    new_db_path = '../data/whoisip.sqlite'
    conn_new = sqlite3.connect(new_db_path)
    c_new = conn_new.cursor()

    # creat a new table
    c_new.execute('''CREATE TABLE IF NOT EXISTS ip_info (
                        ip TEXT PRIMARY KEY,
                        asn TEXT,
                        country TEXT,
                        nic_hdl TEXT
                    )''')

    # find all IP in RP database
    c_source.execute('''SELECT DISTINCT host FROM log''') 
    ip_list = c_source.fetchall()

    # bind IP and whois info
    for ip_tuple in ip_list:
        ip = ip_tuple[0]
        try:
            asn, country, nic_hdl = get_whois_info(ip)
            c_new.execute('''INSERT INTO ip_info (ip, asn, country, nic_hdl)
                             VALUES (?, ?, ?, ?)''', (ip, asn, country, nic_hdl))
        except Exception as e:
            print(f"Error retrieving WHOIS info for {ip}: {e}")

    # close connection
    conn_new.commit()
    conn_new.close()
    conn_source.close()


def main():
    ipdb()

if __name__ == "__main__":
    main()