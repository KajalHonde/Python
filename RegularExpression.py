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


 # Predefined classes
    
import re
str=input("enter main string:")
pattern=input("enter pattern:")
matcher=re.finditer(pattern,str)
for m in matcher:
    print(m.start(),"*****",m.group())
    

# Quantifiers

import re
str=input("enter main string:")
pattern=input("enter pattern:")
matcher=re.finditer(pattern,str)
for m in matcher:
    print(m.start(),"*****",m.group())
    

# Match()
import re
str=input("enter main string:")
pattern=input("enter pattern:")
m=re.match(pattern,str)

if m!=None:
    print("matched")
    print("start index:",m.start())
    print("end index:",m.end())
else:
    print("Not matched")
    

# fullmatch()
import re
str=input("enter main string:")
pattern=input("enter pattern:")
m=re.fullmatch(pattern,str)

if m!=None:
    print("matched")
    print("start index:",m.start())
    print("end index:",m.end())
else:
    print("Not matched")
    

# search()
import re
str=input("enter main string:")
pattern=input("enter pattern:")
m=re.search(pattern,str)

if m!=None:
    print("matched")
    print("start index:",m.start())
    print("end index:",m.end())
else:
    print("Not matched")

# ^
# $
import re
str=input("enter main string:")
pattern=input("enter pattern:")
m=re.search(pattern,str)

if m!=None:
    print("matched")
    print("start index:",m.start())
    print("end index:",m.end())
else:
    print("Not matched")
    
    

# findall()
import re
str=input("enter main string:")
pattern=input("enter pattern:")
m=re.findall(pattern,str)

if m!=None:
    print("matched")
else:
    print("Not matched")
  

  
# finditer()
import re
str=input("enter main string:")
pattern=input("enter pattern:")
m=re.search(pattern,str)

if m!=None:
    print("matched")
    print("start index:",m.start())
    print("end index:",m.end())
else:
    print("Not matched")
    

# subn()
import re
s=re.sub("[a-z]","#","kajalKAJALkajal")
print(s)

'''
# split()
import re
s="python is easy"
s1=re.split("/",s)
print(s1)