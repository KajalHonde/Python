# using compile() method
'''
import re
pattern=re.compile("t")
matcher=pattern.finditer("Python is easy to learn and usee, that's why like python")
count=0
for m in matcher:
    print("start index:",m.start())
    print("match word",m.group())
    # print("occurence of t:",matcher.count("t"))
    print("end index",m.end())
    count+=1
print(count)


# without using compile
import re
count=0
matcher=re.finditer("k","kajal is king and good loking")
for m in matcher:
    print("start index:",m.start())
    print("match word",m.group())
    print("end index",m.end())
    count+=1
print(count)


import re
str=input("enter main string:")
pattern=input("enter pattern:")
matcher=re.finditer(pattern,str)
count=0
for m in matcher:
    print("start index:",m.start())
    print("match word",m.group())
    print("end index",m.end())
    count+=1
print(count)


# character classes

import re
str=input("enter main string:")
pattern=input("enter pattern:")
matcher=re.finditer(pattern,str)
for m in matcher:
    print(m.start(),"*****",m.group())
    
'''

 # Predefined classes
    
import re
str=input("enter main string:")
pattern=input("enter pattern:")
matcher=re.finditer(pattern,str)
for m in matcher:
    print(m.start(),"*****",m.group())