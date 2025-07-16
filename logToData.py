def lineToRecord(line: str) -> list[str] :
    fields = []
    chari = 0

    # get IP address
    part = getField(line, chari, ' ')
    fields.append(part[0])
    chari = part[1] + 3

    # country code
    part = getField(line, chari, ' ')
    fields.append(part[0])
    chari = part[1] + 4
    
    # time
    part = getField(line, chari, ']')
    fields.append(part[0])
    chari = part[1] + 3

    # request
    part = getField(line, chari, '"')
    fields.append('"'+ part[0] +'"')
    chari = part[1] + 2

    # status
    part = getField(line, chari, ' ')
    fields.append(part[0])
    chari = part[1] + 1

    # 1234
    part = getField(line, chari, ' ')
    fields.append(part[0])
    chari = part[1] + 2

    # blank
    part = getField(line, chari, '"')
    fields.append(part[0])
    chari = part[1] + 3

    # agent
    part = getField(line, chari, '"')
    fields.append('"'+ part[0] +'"')
    chari = part[1] + 2

    # num
    buffer = ""
    while (chari < len(line)):
        buffer += line[chari]
        chari += 1
    fields.append(buffer)
    
    return fields

def getField(line: str, i: int, stop: str) -> tuple[str, int]:
    buffer = ""
    while (line[i] != stop):
        buffer += line[i]
        i += 1
    #print(i, " ", len(buffer))
    return (buffer, i)

'''
print ( ",".join (lineToRecord (
    "100.34.17.233 - NO - [01/07/2025:06:00:02] \"GET /news/grammy-nominations-2024 HTTP/1.1\" 302 1234 \"-\" \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\" 269"
)))
'''


# open log file
rawLog = open("sample-log.log", "r")

# create csv
out = open("trafficLog.csv", "w")
out.write("ip,country,time,request,status,size,blank,agent,num")

# write csv file
for l in rawLog:
    out.write(",".join(lineToRecord(l)))

rawLog.close()
out.close()
