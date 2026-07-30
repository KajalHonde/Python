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
'''
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