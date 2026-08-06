#  enumerate properties
'''
from threading import *
import time

print("Current thread is :",current_thread().name)
current_thread().name="Fortune"
print("Current thread is :",current_thread().name)



def f1():
    for i in range(3):
        time.sleep(2)
        print("child thread name:",current_thread().name)
        
        
t=Thread(target=f1)
t.start()

for i in range(3):
    time.sleep(2)
    print("Main thread is:",current_thread().name)


# ident  unique identification number for each thread

print("main thread ident",current_thread().ident)
print("child thread ident:",t.ident)  


# active_count
print("no of thread currently running",active_count())

def f1():
    for i in range(3):
        time.sleep(2)
        print("child thread name:",current_thread().name)
        
        
t=Thread(target=f1)
t.start()

print("no of thread currently running",active_count())


# enumerate()

def f1():
    for i in range(3):
        time.sleep(2)
        print("child thread name:",current_thread().name)
        
def f2():
    for i in range(3):
        time.sleep(2)
        print("child thread name:",current_thread().name)
        
t=Thread(target=f1)
t=Thread(target=f2)
l=enumerate()
print(l)
# t.start()
# t.start()
for th in l:
    print(th.name)
    print(th.ident)
    print()

# is_alive()

def f1():
    for i in range(3):
        print(current_thread().name,"started")
        time.sleep(2)
        print(current_thread().name,"stopped")
        
def f2():
    for i in range(3):
        print(current_thread().name,"started")
        time.sleep(2)
        print(current_thread().name,"stopped")
        

th1=Thread(target=f1,name="python")
th2=Thread(target=f2,name="python")

th1.start()
th2.start()
print("Is alive:",th1.is_alive())
print("Is alive:",th2.is_alive())

time.sleep(9)
print("Is alive:",th1.is_alive())
print("Is alive:",th2.is_alive())
    

# join ()

def f1():
    for i in range(3):
        time.sleep(2)
        print("child thread name:",current_thread().name)
        
th1=Thread(target=f1,name="python")
th1.start()
th1.join(3)
print("end of application")

# Daemon Thread()

from threading import *
import time
print("Is main thread daemon:",current_thread().daemon)

def f1():
    for i in range(3):
        time.sleep(2)
        print("child thread name:",current_thread().name)
        
th1=Thread(target=f1)

th1.daemon=True
th1.start()
print("Is child thread daemon:",th1.daemon)

'''
from threading import *
import time

def exam():
    for i in range(1,10):
        print("class",i)
        time.sleep(2)
        
        
t1=Thread(target=exam)
t1.daemon=True
t1.start()
time.sleep(7)
print("Exams finished")