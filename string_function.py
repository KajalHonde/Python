#rstrip(): removes right hand space
#lstrip(): removes left hand sside spaces
#strip():to remove spaces from both side
'''
state=input("enter state:")
state.lstrip()
if state=="mahrashtra":
    print("captial:mumbai")
elif state=="goa":
    print("panji")
elif state=="karnataka":
    print("banglore")
else:
    print("invalid state")
  
    
    #findinng substring
str1=input("enter main string")
str2=input("enter substring to find")
#x=str1.find(str2)
#x=str1.index(str2)
x=str1.rfind(str2)
print(x)
 
s1="python is easy to learn"
s2="y"
x=s1.find(s2,5,15)
print(x)


 #counting string function
 
str1=input("enter main string")
str2=input("enter sub string")
x=str1.count(str2)
x=str1.count(str2,3,13)
print(x)

 
 #replace function
s1="python is easy"
s2=s1.replace("python","java")
print(s2)

#splitinng string
s="kajalismyname"
s1=s.split("j")
for i in s1:
 print(i)
 
w="22-03-2004"
k=w.split("-")
print(k)


'''
#join 
s1="how are you"
s2="-".join(s1)
print(s2)

li=["python","java","c"]
s1=" ".join(li)
print(s1)

li=["python","java","c"]
s1="-".join(li)
print(s1)