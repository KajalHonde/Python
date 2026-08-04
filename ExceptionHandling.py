'''
print("hello")

n1=10
n2=0
n3=n1/n2
print(n3)

n1=int(input("enter numerator"))
n2=int(input("enter denominator"))
try:
    n3=n1/n2
    print(n3)
except ValueError:
    print("A number has to be an integer")
except ZeroDivisionError:
    print("Number can't be divided by zero")
except NameError:
    print("Define variable before usses")
except:
    print("divion not possible")

print("End of application")


n1=int(input("enter numerator"))
n2=int(input("enter denominator"))
try:
    n3=n1/n2
    print(n3)
except(ZeroDivisionError,NameError,ValueError) as msg:
    print("Error",msg)
except:
    print("Something  went wrong")
    

try:
    n1=int(input())
    n2=int(input())
    n3=n1/n2
    print(n3)
# except ZeroDivisionError:
#     print("It can't be divided by zero")
except ArithmeticError:
    print("Its Arithimetic error")
except ValueError:
    print("its value error")
except ZeroDivisionError:
    print("It can't be divided by zero")
except:
    print("some other error")
print("End of the application")


try:
    n1=int(input())
    n2=int(input())
    n3=n1/n2
    print(n3)
except ZeroDivisionError:
    print("It can't be divided by zero")
    
finally:
    print("clean up activity")
    

try:
    n1=int(input())
    n2=int(input())
    n3=n1/n2
    print(n3)
except ZeroDivisionError:
    print("It can't be divided by zero")  
else:
    print("all done")
finally:
    print("clean up activity")
    
print("End of application")

'''
# user defined exception

class MyException(Exception):
    def __init__(self,message):
        self.message=message
class Bank:
    def __init__(self,actno,balance=500):
      self.actno=actno
      self.balance=balance
    #   self.withdraw=0
      self.deposit=0
      
    def withdraw(self,amount):
        if self.balance<amount:
            raise MyException("Insufficient fund available")
        else:
            self.balance=self.balance-amount
            
    def showBalance(self):
        print("Balance =", self.balance)

b1=Bank(101,10000)
print(b1.balance) 
try:   
    b1.withdraw(400)
except MyException:
    print("Insufficient Balance")
print(b1.balance)    
# showBalance()