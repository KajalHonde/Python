#Arthimetic operator
'''
Add
sub
Floor div
modules
multiplication
division

x=200
y=30

c=("Addition",x+y)
print (c)

d=("substraction",x-y)
print(d)

t=("division",x/y)
print(t)

e=("modules",x%y)
print(e)

w=("floor division",x//y)
print(w)

v=("Exponential",x**y)
print(v)

#Relational operators
#(<  <=  >   ==  !=  >=)
a=20
b=10
print(a<b)
print(a<=b)
print(a>=b)
print(a>b)
print(a!=b)
print(a==b)


#logical operators(and,or,not)
#A) boolean
a=70
b=40

#AND
c=a>b and b>30
print(c)

#OR
d=a>b or b<=30
print(d)

#B)non-boolean
#if first value is false it will store first value in c
a,b=10,20
c=a and b
s=a<b and b-30
q=b-30 and  a-a
w= a-a and b<50
print(c)
print(s)
print(q)
print(w)


#string 
a=""
b="java"
c= a and b
print(c)

#boolean
print(" " and "Python")

#not
a,b =10,5
#c =not(a<b)  #not (true)
c=not(a)  #not(10) not (true)
c= not("python")  #non true is false
c=not("")
#c= a!=b
print(c)

#bitwise operator
a,b =10,5
print(a&b)
print(a|b)
print(a ^ b)

#a=False
a=-2
print(~a)


#left shift << the bits move towards left side

a=True
print(a>>2)

#right shift
print(a<<2)

a=10
print(a<<2)
print(a>>2)


#Assignment operator
#(+= , -= , *= , %= , **= , |= , >>= , <<= , ^= , &= , //= , /= , )

a=10
b=5

#a+b
a+=b
print(a)

a-=b
print(a)

a*=b
print(a)

a**=b
print(a)

a|=b
print(a)

a>>=b
print(a)

a<<=b
print(a)

a//=b
print(a)

a/=b
print(a)

a%=b
print(a)

#ternary operator
a,b = 10,5
x=30 if a<b else 40
print(x)

a,b = 70,50
a if a<=b else b
print(a)


n1=40
n2=30
print("n1 is max") if n1>=n2 else print("n2 is greater")


age=15
print("person is eligible") if age>=18 else print("person is not eligible")


num =24
print("num is odd") if num % 2 != 0 else print("num is even") 

#special operators
# 1. ID operator
n1=[10,20,30,40]
n2=[10,20,30,40]
print(id(n1))
print(id(n2))

print(n1 is n2)
print(n1 is not n2)

n1=10
n2=10
print(n1 is n2)
print(n1 is not n2)

'''

#Membership operator : to check members
s1 ="python is easy"
s2 ="on"
print(s2 in s1)
s2= "on"
print(s2 not in s1)
