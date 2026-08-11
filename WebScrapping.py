# Process of collecting information from web pages
import re
import urllib, urllib.request

s="https://www.fortunecloudindia.com"
u=urllib.request.urlopen(s)
data=u.read()
l=re.findall("<title>.*</title>",str(data),re.IGNORECASE)
print(l)