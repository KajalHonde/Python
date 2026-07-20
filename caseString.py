'''
#changing case of string
s1="python is easy"
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.capitalize())
print(s1.title())


#string checking
#1. startswith(substring)
#2. endswith(substring)
s1="python is easy to learn"
print(s1.startswith("python"))
print(s1.endswith("learn"))


#checking what type  of character it is
s1=("python123")
print(s1.isalnum())

s2=("python")
print(s2.isalpha())

s3=("1234")
print(s3.isdigit())

s4=("PYTHON")
print(s4.isupper())

s5=("pythion")
print(s5.islower())

s6=("Hello This Is Kajal")
print(s6.istitle())

s7=("  ")
print(s7.isspace())

s=input("Enter the string to check its type")

if s.isalnum():
    print("alpha numeric value")
elif s.isalpha():
    print("alphabetic value")
elif s.istitle():
    print("title value")
elif s.isupper():
    print("upper value")
elif s.islower():
    print("lower value")
else :
    print("invalid output")
    


#reverse string
s=input("enter string")
print(s[::-1])


s1="python is easy"
s2=s1.split()
print(s2)
s3=s2[::-1]
print(s3)
s4=" ".join(s3)
print(s4)
'''
#merging two charaters
str1=input("enter the string : ")
str2=input("enter secoond string: ")
output=''

i=0
j=0

while i<len(str1) or j<len(str2):
    if i<len(str1):
        output=output+str1[i]
        i=i+1
    if j<len(str2):
        output=output+str2[j]
        j=j+1
        
print(output)
    