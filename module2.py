'''
# 1st method
import module1

module1.add()
module1.sub()

print("y is",module1.y)

# 2nd method
from module1 import add
add()

# 3rd method
# aliasing
import module1 as n1
n1.add()
n1.sub()



# dir(): gives current files data
a=10
b=20

def factorial():
    pass
'''
import string
# print(math.pi)
# print(dir(math))
print(string.ascii_letters)