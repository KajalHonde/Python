'''
class Test:
    x=10
    def __init__(self):
        self.a=100
        print(self.x)
        
    def m1(self):
        print("a",self.a)
        
    
    # @classmethod
    def clsmthd(cls):
        print("this is class method")
        print("cls",cls.x)
        print("printing cls",cls)
        print("className",Test.x)

# Test.clsmthd()
t=Test()
t.m1()
t.clsmthd()

'''
# static method

class Math:
    @staticmethod
    def add(x,y):
        print(x+y)
        
# m=Math()
Math.add(10,5)
M=Math()
M.add(10,3)
