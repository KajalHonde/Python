'''
class Student:
    def __init__(self):
       
        print("This is constructor")
        self.a=10
        self.b=10
        
    # a=10
    # b=5
    
    def add(self):
        print("This is addition of",self.a+self.b)
        
def sub():
    print("substraction is :",s1.a-s1.b)
    
s1=Student()
s1.add()        
sub()

s2=Student()
s2.add()
s1.add()  


class Student1:
    def __init__(self):
        pass
    
def add(s1,n2):
        print("Addition of two numbers is ",n1+n2)
        
s1=Student1()        
n1=int(input("enter the num1"))
n2=int(input("enter the num2"))

add(n1,n2)


# Types of constructors:

# constructor with parameters

class Student2():
    def __init__(self,n1,n2):
        self.x=n1
        self.y=n2
    
    def add(self):
        print("addition",self.x+self.y)
        
n1=int(input("num1 is:"))
n2=int(input("num2 is:"))

s1=Student2(n1,n2)
s1.add()



# constructor without parameters
class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.salary=salary
        self.age=age
        
    def employee_data(self):
        print("Employee age is:",self.name)
        print("Employee age is:",self.salary)
        print("Employee age is:",self.age) 
        
name=input("enter name")
salary=int(input("enter salary"))
age=int(input("enter age"))
        
emp1=Employee(name,age,salary)
emp1.employee_data()

emp2=Employee(name,age,salary)
emp2.employee_data()

# instance variable

class Test():
    def __init__(self):
        self.a=10
    
    def m1(self):
        self.b=20
    
    def show(self):
        print("a=",self.a)
        print("b=",self.b)
        
t1=Test()
t1.m1()
t1.show()
print("t1 ..insance variables",t1.__dict__)
t2=Test()
print("t2 instance variables are",t2.__dict__)
t2.m1()
print("t2 instance variabls are ",t2.__dict__)


# static variable

class Student():
    loc="yeola"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print("name",self.name)
        print("age",self.age)
        print("location",self.loc)
        
print("location is",Student.loc)
s1=Student("kajal",22)
s2=Student("priya",21)

s1.show()
s2.show()
Student.loc="Manmad"
s1.show()
s2.show()


class Test:
    a=10
    def __init__(self):
        self.b=20
       
       
print("a",Test.a)
t1=Test()
t2=Test()

print(t1.a,"and",t1.b)
print(t2.a,"and",t2.b)

Test.a=100
t1.b=203
print(t1.a,"and",t1.b)
print(t2.a,"and",t2.b)
t1=Test()
print("a",Test.a)
# print("b",self.b)
t=Test()
print(t1.b)
print(c)


# declaring static variable
'''
class Test:
    a=10
    count=0
    
    def __init__(self):
        Test.count+=1
        Test.b=90
          
    def t1(self):
        Test.c=30
        print(Test.c)
        
    @classmethod
    def clsmthd(cls):
        Test.d=73
        print(Test.d)
        del cls.a
        
    @staticmethod
    def stsmthd():
        Test.f=40
        print(Test.f)
        
        
t=Test()
t1=Test()
print("a",Test.a)

print(t.b)

t.t1()
t.stsmthd()
t.clsmthd()

print(Test.count)

# deleting static variable
# del Test.a
# print(Test.a)
