'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
        

class Test:
    def __init__(self,branch,name,salary):
        self.branch=branch
        self.emp=Employee(name,salary)
        
    def show(self):
        print("name:",self.emp.name)
        print("salary",self.emp.salary)
        print("Branch:",self.branch)
        
t1=Test("AIML","kajal",20000)
t1.show()

'''
class Car():
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
    
    def carInfo(self):
        print("Car Nam:",self.name)
        print("Car model is:",self.model)
        print("car color:",self.color)
        
c=Car("audi",123,"white")
c.carInfo()

class Employee():
    def __init__(self, eno, ename, car):
        self.eno=eno
        self.ename=ename
        self.car=car
    
    def einfo(self):
        print("eno:",self.eno)
        print("ename:",self.ename)
        
        print("emp car details are:")
        self.car.carInfo()
        
c=Car("Audi",0000,"black")
e=Employee(1,"Kajal",c)
e.einfo()