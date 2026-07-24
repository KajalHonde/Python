class Test():
    def show(self):
        print(self)
        self.a=10
        self.b=3
    def display(self):
        print("a=",self.a)
        print("b=",self.b)
    
t1=Test()
t1.show()
t1.display()
print("************************")
t2=Test()
t2.show()
t2.display()