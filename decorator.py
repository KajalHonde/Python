'''
def decorator (func):
    def inner(name):
        if name=="guest":
            print("Dear guest you need to register yourself")
        else:
            func(name)
            
    return inner
            
            
@decorator
def wish(name):
    print("hello",name)
    
    
wish("kajal")
wish("guest")

n1=90
n22=0
print(n1/n22)

def decorator (func):
    def inner(n1,n2):
        if n2==0:
            print("Number can't be divided")
        else:
            func(n1,n2)
            
    return inner

@decorator
def divide (n1,n2):
    print(n1/n2)

# print(divide(10,0))

divide(10,0)
divide(10,2)


# using decorator without  calling it with "annotatio"
def decorator (func):
    def inner(name):
        if name=="guest":
            print("Dear guest you need to register yourself")
        else:
            func(name)
            
    return inner
 
 
def wish(name):
     print("hello",name)
        
dfunction=decorator(wish)
dfunction("tom")
            
'''
# decorator chaining
def decor1(func):
    def inner(name):
        print("first decor")
        func(name)
    return inner

def decor2(func):
    def inner(name):
        print("second decor")
        func(name)
    return inner

@decor1
@decor2
def  wish(name):
    print("hello",name)
    
wish("kajal")