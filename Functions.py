'''
print("Good evening")
def show():
    print("This is show")
    return

def display():
    print("this is display function")
    return


display()
show()
display()
print("end of an application")
show()

print("Good evening")
def show():
    print("hi")
    display()
    print("This is show")
    

def display():
    print("this is display function")

show()
print("End of the application")

def add():
    n1=int(input("enter num1"))
    n2=int(input("enter num2"))
    n3=n1+n2
    print("sum of num1 and num2 is",n3)
    
add()

# Aliasing functions
def wish(name):
    print("hello i'm",name)    
wish(input("Enter the Name :"))

greeting=wish
greeting(input("enter name: "))

print(id(greeting))
print(id(wish))

# Nested function
# 1st way
def outer():
    print("outer function starts")
    
    def inner():
        print("start of inner function")
    inner()
    print("outer function ends")

outer()

# 2nd way

'''
def outer():
    print("outer function starts")
    
    def inner():
        print("start of inner function")
    print("outer function ends")
    return inner

inn=outer()
inn()