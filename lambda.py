# Normal Function
'''
def square(x):
    s=x*x
    return s

r=square(6)
print(r)

# using lambda
square=lambda x: x*x
print(square(5))

square=lambda x,y: x+y
print(square(5,4))

max=lambda x,y: x if x>y else y
print(max(2,4))

# built in functions used with lambda
# 1.filter()
# Normal

def iseven(x):
    if x%2==0:
        return True
    else:
        return False
    
print(iseven(int(input())))

l1=[10,20,3,7,5,8,9,4,2]
f=list(filter(iseven,l1))


iseven=lambda x: True if x%2==0 else False
l1=[10,20,3,7,5,8,9,4,2]
f=list(filter(iseven,l1))
print(f)

# print(iseven(int(input())))

l=['t','u','t','o','r','i','a','l']
exceptt=lambda l: True if l != 't' else False
f=list(filter(exceptt,l))
print(f)


#2. Map()
# normal function
def double(x):
    return 2*x

l1=[2,3,4,5]
m=list(map(double,l1))
print(m)

# lambda
l1=[2,3,4,5]
l2=[1,2,3,4]
m=lambda x,y: y*x
print(list(map(m,l1,l2)))
'''
from functools import *
l1=[10,20,30,40,50]
result=(reduce(lambda x,y: x+y,l1))
print(result)

result=(reduce(lambda x,y: x*y,l1))
print(result)