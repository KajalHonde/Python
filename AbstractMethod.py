from abc import *

# class with abstract method
class Employee(ABC):
    @abstractmethod
    def calofsal(self):
        pass
    
    def empdetail(self):
        print("Details of employee")
        
# e1=Employee()
# e1.empdetail()

# Abstract class without abstract method
class Employee(ABC):
    def empdetail(self):
        print("Details of employee")
        
# class with abstarct method
class Employee:
    @abstractmethod
    def calofsal(self):
        pass
    
    def empdetail(self):
        print("Details of employee")
        
e=Employee()
e.empdetail()