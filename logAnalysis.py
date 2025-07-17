import pandas as pd

# read csv
df = pd.read_csv('trafficLog.csv')

# display top 10 most active IPs
ipCount = df.groupby("ip").size().nlargest(n=20)

# display requests from the found addresses
rus = df[ df["ip"].str.contains("45.133.1.") ]
us = df[ df["ip"] == "35.185.0.156" ]

uk = df[ df["ip"].str.contains("194.168.1.") ]
crossCon = df[ df["ip"].str.contains("185.220.10") ]


# investigate most requested pages
topPages = df.groupby("page").size().nlargest(n=25)

# podcast episode requests
eps = df[ (df["page"] == "/episodes/ep-42-synthesizer-history HTTP/1.1") ]
epsReq = eps.groupby("ip").size().nlargest(n=10)

# artists requests
art = df[ (df["page"] == "/artists/emerging-indie-artists HTTP/1.1") ]
artReq = eps.groupby("ip").size().nlargest(n=10)

# interviews requests
inter = df[ (df["page"] == "/artists/emerging-indie-artists HTTP/1.1") ]
interReq = eps.groupby("ip").size().nlargest(n=10)


# investigate reoccurring pages from ips
requests = rus.groupby("request").size()

sitesUK = uk.groupby("page").size().nlargest(n=25)
sitesCross = crossCon.groupby("page").size()

# output a table
print(topPages)
