
## coverts a single log into a list of fields

def lineToRecord(line: str) -> list[str] :
    fields = []
    chari = 0

    # get IP address
    part = extractField(line, chari, ' ')
    fields.append(part[0])
    chari = part[1] + 3

    # country code
    part = extractField(line, chari, ' ')
    fields.append(part[0])
    chari = part[1] + 4
    
    # time
    part = extractField(line, chari, ']')
    fields.append(part[0])
    chari = part[1] + 3

    # request type
    part = extractField(line, chari, ' ')
    fields.append(part[0])
    chari = part[1] + 1

    # requessted page
    part = extractField(line, chari, '"')
    fields.append('"'+ part[0] +'"')
    chari = part[1] + 2

    # status
    part = extractField(line, chari, ' ')
    fields.append(part[0])
    chari = part[1] + 1

    # 1234
    part = extractField(line, chari, ' ')
    fields.append(part[0])
    chari = part[1] + 2

    # blank
    part = extractField(line, chari, '"')
    fields.append(part[0])
    chari = part[1] + 3

    # agent
    part = extractField(line, chari, '"')
    fields.append('"'+ part[0] +'"')
    chari = part[1] + 2

    # num
    part = extractField(line, chari, '"')
    fields.append(part[0])
    
    return fields

## iterates through the line until the stop char is reached

def extractField(line: str, i: int, stop: str) -> tuple[str, int]:
    # clean input
    if line == "" or i < 0:
        return ("", 0)
    
    if len(stop) > 1 :
        stop = stop[0]

    buffer = ""
    while (i < len(line) and line[i] != stop):
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
out.write("ip,country,time,request,page,status,size,blank,agent,num\n")

# write csv file
for l in rawLog:
    try:
        out.write(",".join(lineToRecord(l)))
    except:
        break

# close files
rawLog.close()
out.close()
