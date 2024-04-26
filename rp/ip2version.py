import sqlite3
from datetime import datetime


def ip2version(date, ipAdd):

    try:
        # date to datetime transfer
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        
        # date to unix transfer
        unixT = date_obj.timestamp()
        timeStart = str(unixT)
        timeEnd = str(unixT + 172800)
        
        # print("Unix:", int(unixT))
        
    except ValueError:
        return("format error, please input a date like YYYY-MM-DD")
        

    # database connection
    conn = sqlite3.connect('../data/krill1-log.sqlite')

    # build cursor
    cursor = conn.cursor()

    # do SQL
    cursor.execute("SELECT agent FROM log WHERE host =='" + ipAdd + "' AND timestamp >=" + timeStart + " AND timestamp <"+ timeEnd +";")

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
inputIP = input("input an IP address like 34.138.55.103:")


i2v = ip2version(inputDate, inputIP)
print(i2v)
