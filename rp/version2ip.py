import sqlite3
from datetime import datetime


def version2ip(date, rpv):

    try:
        # date to datetime transfer
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        
        # date to unix transfer
        unixT = date_obj.timestamp()
        timeStart = str(unixT)
        timeEnd = str(unixT + 172800)
        
        # print("Unix:", int(unixT))
        
    except ValueError:
        return(["format error, please input a date like YYYY-MM-DD"])
        

    # database connection
    conn = sqlite3.connect('../data/krill1-log.sqlite')

    # build cursor
    cursor = conn.cursor()

    # do SQL
    cursor.execute("SELECT host, agent FROM log WHERE agent GLOB '" + rpv + "*' AND timestamp >=" + timeStart + " AND timestamp <"+ timeEnd +";")

    # get result
    rows = cursor.fetchall()

    # output
    output = []
    for row in rows:
        if row not in output:
            output.append(row)

    # close cursor and connection
    cursor.close()
    conn.close()

    return(output)

# input a date
inputDate = input("input a date like YYY-MM-DD:")

# input an IP address
inputVersion = input("input an IP address like Routinator/0.11.0:")


v2i = version2ip(inputDate, inputVersion)
for item in v2i:
    print(item)
