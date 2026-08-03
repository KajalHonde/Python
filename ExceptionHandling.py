'''
print("hello")

n1=10
n2=0
n3=n1/n2
print(n3)
'''
n1=int(input("enter numerator"))
n2=int(input("enter denominator"))
try:
    n3=n1/n2
    print(n3)

except ZeroDivisionError:
    print("Number can't be divided by zero")
except:
    print("divion not possible")