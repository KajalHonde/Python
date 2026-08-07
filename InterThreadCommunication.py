from threading import *
import time
'''
# Using Event class

e=Event()
def producer():
    time.sleep(5)
    print("producer thread producing item")
    time.sleep(5)
    print("producer thread givinng notificatons by seeting event")
    e.set()
    
def consumer():
    print("consumer threa waiting for updation")
    e.wait()
    time.sleep(2)
    print("consumer got notification and consuming items")

t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()

# using condition object

c=Condition()

def consumer():
    c.acquire()
    print("consumer threa waiting for updation")
    time.sleep(3)
    c.wait()
    print("consumer got notification and consuming items")
    c.release()
    
    
def producer():
    c.acquire()
    print("producer producig")
    time.sleep(10)
    print("producer thread givinng notifications")
    # time.sleep(3)
    c.notify()
    c.release()
    
t1=Thread(target=consumer)
t2=Thread(target=producer)
t1.start()
t2.start()

'''
# using Queue
from threading import *
import time
import random
import queue

q=queue.Queue()

def producer():
    while True:
        item=random.randint(1,100)
        print("producer producing item",item)
        q.put(item)
        print("producer giving notifications")
        time.sleep(3)
        
def consumer():
    while True:
        print("consumer waiting foor updation")
        print("consumer consuming items", q.get())
        time.sleep(4)
        
t1=Thread(target=consumer)
t2=Thread(target=producer)
t1.start()
t2.start()