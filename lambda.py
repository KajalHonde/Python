# Normal Function
'''
def square(x):
    s=x*x
    return s

r=square(6)
print(r)
'''
# using lambda
square=lambda x: x*x
print(square(5))

square=lambda x,y: x+y
print(square(5,4))

max=lambda x,y: x if x>y else y
print(max(2,4))