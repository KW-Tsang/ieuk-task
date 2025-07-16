import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read csv
df = pd.read_csv('trafficLog.csv')

# display top 10 most active IPs
ipCount = df.groupby("ip").size().nlargest(n=10)

# display requests from the found addresses
rus1 = df[ df["ip"] == "45.133.1.1" ]
rus2 = df[ df["ip"] == "45.133.1.2" ]
us = df[ df["ip"] == "35.185.0.156" ]

# see commonalitys between requests
agents = rus2.groupby("agent").size()
requests = rus1.groupby("request").size()

# investigate most requested pages
pages = df.groupby("page").size().nlargest(n=25)

# podcast episode requests
eps = df[ (df["page"] == "/episodes/ep-42-synthesizer-history HTTP/1.1") ]
epsReq = eps.groupby("ip").size().nlargest(n=10)

# artists requests
art = df[ (df["page"] == "/artists/emerging-indie-artists HTTP/1.1") ]
artReq = eps.groupby("ip").size().nlargest(n=10)

# interviews requests
inter = df[ (df["page"] == "/artists/emerging-indie-artists HTTP/1.1") ]
interReq = eps.groupby("ip").size().nlargest(n=10)

print(interReq)
