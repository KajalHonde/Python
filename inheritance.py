'''
class Parent:
    a=10
    def __init__(self):
        self.b=20
    
    def m1(self):
        print("Parent instance method")
        
    @classmethod
    def m2(cls):
        print("parent class method")
        
    @staticmethod
    def m3():
        print("parent static method")
        

class Child(Parent):
    pass

c1=Child()
print(c1.a)
print(c1.b)
c1.m1()
c1.m2()
c1.m3()

class Parent:
    def __init__(self):
        print("Parent Constructor")
        self.a=10
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.b=20
        
    def m1(self):
        print("Addition",self.a+self.b)
      
c1=Child()  
c1.m1()

# Types of inheritance
# Multi-level inheritance

class Gparent:
    def __init__(self):
        self.a=10
        print("Gparent constructor")
        
class Parent(Gparent):
    def __init__(self):
        self.b=20
        super().__init__()
        print("Parent Constructor")
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
    def add(self):  
        print("addition of a and b is:", self.a+self.b)
        
c1=Child()
c1.add()

# Multiple Innheritance

class Parent1:
    def add(self):
        self.a=10
        self.b=5
        print("addition",self.a+self.b)
     
class Parent2:
    def sub(self):
        self.q=30
        self.w=20
        print("substraction",self.q-self.w)
        
class Child(Parent1,Parent2):
    pass
           
c1=Child()
c1.sub()
c1.add()
     
'''
# Heirachical inheritance

class Parent:
    def __init__(self):
        self.a=10
        self.b=5
        
class Child1(Parent):
    def add(self):
        print("Addition:",self.a+self.b)
        
class Child2(Parent):
    def sub(self):
        print("Substraction:",self.a-self.b)

c1=Child1()
c1.add()
c2=Child2()