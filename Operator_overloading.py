class Books:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self, other):
        print(self.pages)
        print(other.pages)
        pgs=self.pages+other.pages
        return Books(pgs)
    # def __mul__(self,other):
    #     print(self.b1,other.b2)
    #     return self.b1*self.b2
    
b1=Books(200)
b2=Books(300)
b3=Books(100)
b4=b1+b2+b3
print(b4.pages)
# print(b1*b2)
