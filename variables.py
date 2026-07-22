'''
# local variable
def f():
    a=10
    print(a)
    
def f1():
    print(a)
    
f()
f1()

# In function Global variable
# a=10
def f():
   global a
   a=10
   print(a)
    
def f1():
    print(a)
    
f()
f1()
'''
# global and local variable together

a=100
def f1():
    a=40
    print(a)
    print("global a:",globals()['a'])

f1()