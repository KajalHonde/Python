from threading import *
import time
'''
# Using Lock()
l=Lock()
def test(name):
    l.acquire()
    for i in range(3):
      print("Hello",name)
      time.sleep(2)
    l.release()
    
    
t1=Thread(target=test,args=("Kajal",))
t2=Thread(target=test,args=("Komal",))

t1.start()
t2.start()
t1.join()
t2.join()

print("End of program")

# Using RLock()

l=RLock()
def factorial(n):
    l.acquire()
    if n==1 or n==0:
        f=1
    else:
        f=n*factorial(n-1)
    l.release()
    return f

def result(n):
    print("Factorial is",factorial(n))
    
th1=Thread(target=result,args=(5,))
th1.start()
th1=Thread(target=result,args=(6,))
th1.start()

'''

l=Semaphore(2)
def test(name):
    l.acquire()
    for i in range(3):
      print("Hello",name)
      time.sleep(2)
    l.release()

    
th1=Thread(target=test,args=("kajal",))
th1.start()
th2=Thread(target=test,args=("Priya",))
th2.start()
th3=Thread(target=test,args=("Komal",))
th3.start()
th4=Thread(target=test,args=("Atul",))
th4.start()
th5=Thread(target=test,args=("Shivani",))
th5.start()
th6=Thread(target=test,args=("Kunal",))
th6.start()
th7=Thread(target=test,args=("Kalyani",))
th7.start()

