class Animal:
    def sound(self):
        print("Animal Sound")
        
class Bird():
    def sound(self):
        print("Bird sound")
        
class Pets():
    pass
    # def sound(self):
    #     print( "Pets sound")
        
class Retrieve():
    def __init__(self,obj):
        obj.sound()
'''       
r1=Retrieve(Animal())

Retrieve(Animal())

a1=Animal()
r2=Retrieve(a1)
'''

l1=[Animal(),Bird(),Pets()]
for obj in l1:
    if hasattr(obj,"sound"):
       obj.sound() 
    else:
        print("Object has no sound")