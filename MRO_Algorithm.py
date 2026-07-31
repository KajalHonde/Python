class Parent1:
    def m1(self):
        print("This is parent 1 m1")
        

class Parent2:
    def m1(self):
        print("This is parent 2 m1")
        
class Child(Parent1,Parent2):
    pass
    # def m1(self):
    #     print("This is child m1")
 
 
'''
class Child(Parent2,Parent1):
    pass
    # def m1(self):
    #     print("This is child m1")
'''
       
c1=Child()
c1.m1()
print(Child.mro())