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
'''

n1=int(input("enter numerator"))
n2=int(input("enter denominator"))
try:
    n3=n1/n2
    print(n3)
except(ZeroDivisionError,NameError,ValueError) as msg:
    print("Error",msg)
except:
    print("Something  went wrong")