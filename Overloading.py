'''
class Books:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self, other):
        print(self.pages)
        print(other.pages)
        pgs=self.pages+other.pages
        return Books(pgs)
   
    
b1=Books(200)
b2=Books(300)
b3=Books(100)
b4=b1+b2+b3
print(b4.pages)

class Employee:
    def __init__(self,name,salperday):
        self.name=name
        self.salperday=salperday
        
    def __mul__(self,other):
        return self.salperday * other.noofdays
        
class Timesheet:
    def __init__(self,name,noofdays):
        self.name=name
        self.noofdays=noofdays
        
e=Employee("kajal",35000)
t=Timesheet("kajal",8)
print(e*t)

# Method overloading
class Math:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif(a!=None and b!=None):
            print(a+b)
            
        else:
            print("Need atleast two arguements")
            
m1=Math()
m1.sum(10,20,40)

'''
class Math:
    def sum(self,*args):
        total=0
        for x in args:
            total+=x
        print("Total",total)
        
        
m1=Math()
m1.sum(10,20,30,40)