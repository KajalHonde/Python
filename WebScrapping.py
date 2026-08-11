# Process of collecting information from web pages
'''
import re
import urllib, urllib.request

s="https://www.fortunecloudindia.com"
u=urllib.request.urlopen(s)
data=u.read()
l=re.findall("<title>.*</title>",str(data),re.IGNORECASE)
print(l)
'''

import re , urllib
import urllib.request
sites=["google","rediff"]
for s in sites:
    print("searching...",s)
    u=urllib.request.urlopen("http://"+s+".com")
    text=u.read()
    title=re.findall("<title>.*</title>",str(text),re.IGNORECASE)
    print(title[0])