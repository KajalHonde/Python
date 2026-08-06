from threading import *
import time
print("Current Thread:",current_thread().name)

'''
def f1():
    for i in range(3):
        print("function 1")
        time.sleep(1)
        
        
def f2():
    for i in range(3):
        print("function 2")
        time.sleep(1)
        
  
for i in range(3):
    print("function ")
    time.sleep(1)
          
# creating thread without class
t=Thread(target=f1)
t.start()
t=Thread(target=f2)
t.start()
        
# f1()
# f2()
print("end of application")


# creating thhread with eextending thread class
class Mythread(Thread):
    def run(self):
        for i in range(3):
            print("Child thread name:",current_thread().name)
            time.sleep(1)
            
t1=Mythread()
t1.start()

for i in range(3):
    time.sleep(1)
    print("Main thread name:",current_thread().name)
 
# creating thhread with eextending thread class without run method

class Mythread(Thread):
    def f1(self):
        for i in range(3):
            print("Child thread name:",current_thread().name)
            time.sleep(1)
            
t1=Mythread()
t1=Thread(target=t1.f1)
t1.start()

for i in range(3):
    time.sleep(1)
    print("Main thread name:",current_thread().name)
    

# creating class without extending

class Mythread():
    def f1(self):
        for i in range(3):
            print("Child thread name:",current_thread().name)
            time.sleep(1)
            
t1=Mythread()
t1=Thread(target=t1.f1)
t1.start()

for i in range(3):
    time.sleep(1)
    print("Main thread name:",current_thread().name)
    
'''  
# executing multiple thread 

from threading import *
import time
class Test(Thread):
    def run(self):
        for i in range(3):
            print(current_thread().name)
            
t1=Test()
t2=Test()
t3=Test()
t4=Test()

t1.start()
t2.start()
t3.start()
t4.start()
