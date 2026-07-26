'''
class Outer:
    def __init__(self):
        print("outer class")
        
    class Inner:
        def __init__(self):
            print("constructor inner class")
            
        def m1(self):
            print("inner class method m1")
            
    def m2(self):
            print("outer class m2")
            
# o=Outer()
# inn=o.Inner()
# inn.m1()

# inn=Outer().Inner()
# inn.m1()
Outer().Inner().m1()

class Outer:
    def __init__(self):
        print("outer class")
        self.inn=self.Inner()
    class Inner:
        def __init__(self):
            print("constructor inner class")
            
        def m1(self):
            print("inner class method m1")
            
    def m2(self):
            print("outer class m2")
            self.inn.m1()

o=Outer()
'''
class Person:
    def __init__(self,name,city,dd,mm,yy):
        self.name=name
        self.city=city
        self.dob=self.DOB(dd,mm,yy)
        
    class DOB:
        def __init__(self,dd,mm,yy):
            self.dd=dd
            self.mm=mm
            self.yy=yy
        
        def dobf(self):
            print(f"dob{self.dd}-{self.mm}-{self.yy}")
            
    def showdetails(self):
        print(f"Name:{self.name}")
        print(f"city{self.city}")
        self.dob.dobf()
        
name=(input("enter name"))
city=(input("enter your city"))
dd=(int(input("enter dd")))
mm=(int(input("enter mm")))
yy=(int(input("enter yy")))

p=Person(name,city,dd,mm,yy)
p.showdetails()