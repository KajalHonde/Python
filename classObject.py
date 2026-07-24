'''
class Test():
    def show(self):
        print(self)
        self.a=10
        self.b=3
    def display(self):
        print("a=",self.a)
        print("b=",self.b)
    
t1=Test()
t1.show()
t1.display()
print("************************")
t2=Test()
t2.show()
t2.display()
'''

# methods with parameters
from math import*
class Math:
    def accept(self,n1,n2):
        self.x=n1
        self.y=n2
    def add(self):
        print("Addition",self.x+self.y)
        
    def sub(self):
        return self.x-self.y
    
    def mult(self,x,y):
        return x*y
        
m1=Math()
n1=int(input("Enter N1"))
n2=int(input("Enter N1"))

m1.accept(n1,n2)
m1.add()
res=m1.sub()
print(res)
r=m1.mult(n1,n2)
print(r)