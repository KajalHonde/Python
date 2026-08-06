# without multi threading
'''
import time
def double(numbers):
    for i in numbers:
        time.sleep(1)
        print("double is",2*i)
        
        
def square(numbers):
    for n in numbers:
        time.sleep(1)
        print("square",n*n)
        
        
numbers=[2,3,4,5,6,7]

begintime=time.time()
print(begintime)

double(numbers)
square(numbers)
endtime=time.time()
print(endtime-begintime)
'''

# with multi threading

from threading import *
import time

def double(numbers):
    for i in numbers:
        time.sleep(1)
        print("double is",2*i)
        
        
def square(numbers):
    for n in numbers:
        time.sleep(1)
        print("square",n*n)
        
        
numbers=[2,3,4,5,6,7]
t1=Thread(target=double,args=(numbers,))
t2=Thread(target=square,args=(numbers,))
        
begintime=time.time()
print(begintime)
t1.start()
t2.start()
t1.join()
t2.join()

endtime=time.time()
print("end time",endtime-begintime)