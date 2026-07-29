'''
import gc

print("Garbage collector is enabled",gc.isenabled())

gc.enable()
print("Garbage collector is enabled",gc.isenabled())

gc.disable()
print("garbage collector is disable",gc.isenabled())
'''

import time
class Test:
    def __init__(self):
        print("constructor")
        
    def __del__(self):
        print("destructor invoked for clean up activity")
        
t1=Test()
time.sleep(5)
print("work done")
t1=None
time.sleep(10)
print("end of application")