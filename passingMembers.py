class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print("constructor")
    
    def display(self):
        print("Employee name is:",self.name)
        print("Employee salary:",self.salary)
        
        
class Test():
    def modify(self,emp):
        print("modified")
        emp.name="kajal"
        emp.salary=emp.salary+30000
        emp.salary=emp.salary-1000
        emp.display()

e1=Employee("john",20000)
e1.display()
print("***************")
t1=Test()
t1.modify(e1)