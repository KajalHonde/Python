class Books:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self, other):
        print(self.pages)
        print(other.pages)
        return self.pages+other.pages
b1=Books(200)
b2=Books(300)
print(b1+b2)