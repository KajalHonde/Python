# private acess modifier
class Parent:
    def __init__(self):
        self.__a=10
    
    def display(self):
        print("a=",self.__a)
        
p1=Parent()
# print(p1.__a)
p1.display()
print(p1.__Parent__a)

'''
# protected
class Parent:
    def __init__(self):
        self._a=10
    
    def display(self):
        print("a=",self._a)
  
  
class Child(Parent):
      def show(self):
        print("a in child",self._a)
          
c1=Child()
c1.show()
p1=Parent()
# print(p1.__a)
p1.display()
'''