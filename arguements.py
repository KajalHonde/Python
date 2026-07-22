'''
# postional arguements
def showa(name,age):
    print(f"{name} is {age} years old")
    
showa("kajal",21)
    

# keyword arguemennts
def showa(name,age):
    print(f"{name} is {age} years old")
    
showa(age=21,name="kajal")


# default arguement
def showa(name,age,sal=150000):
    print(f"{name} is {age} years old and earning {sal}")
    
showa(age=21,name="kajal")

# variable arguement
def show(*n):
    print(n)
    total=0
    for x in n:
        total=total+x
    print(total)
show(10,20,3)

'''
# keyword variable length arguement
def show(**kwargs):
    print(f{kwargs}"")
    
show(name="kajal",age=21)