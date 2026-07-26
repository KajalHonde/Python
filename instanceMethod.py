class Test():
    def __init__(self):
        self.a=100
        self.b=20
        
    def add(self):
        print("addition",self.a+self.b)
        
    def sub(self):
        self.add()
        print("substracton",self.a-self.b)
    
t1=Test()
t1.sub()
# t1.add()