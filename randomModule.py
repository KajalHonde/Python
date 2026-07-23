# Random()

from random import *
'''
print(random())
x=(random)
for i in  range(3):
    print(random())

# Uniform()
print(uniform(1,4))

for i in range(3):
    print(uniform(100,200))
        

# randint
for i in range(3):
    print(randint(100,200))

l1=[10,20,"python","java",60,70,80]
x=choices(l1,k=2)
print(x)

# randrange(start,end,stop)
for i in range(3):
    print(randrange(100,200,5))
    

# shuffle()
l1=[10,20,30,40,50,60]
shuffle(l1)
print(l1)

# triangular
print(triangular(100,200,4))


# generating otp
print(randint(0,9),chr(randint(65,90)),chr(randint(65,90)),randint(0,9),randint(0,9),randint(0,9),sep="")

for i in range(5):
    print(randint(65,90),chr(randint(65,90)),randint(0,9),randint(0,9),randint(0,9),sep="")
    
'''
import random
import string

def randomstringDigit(strlen=2):
    lettersAndDigits=string.ascii_letters+string.digits
    return "".join(random.choice(lettersAndDigits) for i in range(strlen))

print(randomstringDigit(5))