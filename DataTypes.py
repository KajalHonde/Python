'''
a=20
b=21
#Integer Data
print(a+b)  #addition
print(a-b)  #subs
print(a*b)  #mult
print(a/b)  #div
print(a%b)  #modulus= gives remainder
print(a//b) #floor divion =removes decimal part
print(a**b) #power = 20 multiplied 21 times

#Float Data 
c=24.4
d=5.5

#add
print(c+d)

#round() function: takes to the nearest whole num
print(round(d))

#type() function: shows the dataType of the value
print(type(c))

#complex datatype shows imaginary part 
#.real and .imag are the attributes
z= 3+2j
print(z.real)
print(z.imag)

#float data type
a= 12.9
type(a)

# * used for repetation
#rule is one should be intger
s1 = "python is very easy"
print(s1 * 2)

# + used for contetnation 
# rule is both data should have same data type
s1 = "python is very easy"
s2 = "hello" 
print(s1 + s2)

#bytes
x=[2,3,4,5]
print(x)
print(type(x))

b=bytes(x)
print(b)
print(type(b))
#slicing and indexing allowed 
print(b[1])
print(b[0:3])

#bytes are immutable, so it will give error while changing value


#Byte Array --mutable
y = [10,20,30,40,50]
c=bytearray(y)
print(c)
print(type(c))

print(c[1])
print(c[0:3])
c[0]=100
print(c)
print(type(c))

#List --mutable
#hetrogenous data type because it store diff types of data
l1 = [10,20,30,40,50]
l2 = [10,20,30,40,50]
print(l1)
print(id(l1))
print(l2)
print(id(l2))
print(l1+l2)

# same data type can be added only
x=100
y=200
print(x+y)

# * is used for reptiation
print(l1*4)

a=[10,20,"python",True]
print(a[2])

#adds at the end
a.append("hello")
print(a)

a.remove(True)
print(a)
print(type(a))

#tuple data type

t= (10,20,30,40)
print(t)
print(t[2])
print(t[1:3:1])
print(type(t))

# list in tuple

p=(10,20,30,[40,60])
print(type(p))
print(p[3][1])
print(type(p[3]))

#Range
#A.range(n1)

x=range(10)
print(x)
for i in x:
    print(i)
  
#B.range(n1,n2) 
x=range(1,8)
print(x)
for i in x:
    print(i)
    
   
#c.range(n1,n2,step) 
x=range(1,8,2)
print(x)
for i in x:
    print(i)
    
'''

#SET
s1={1,200,'python',400,'java'}
s1.add('c++')
s1.remove(200)
print(s1)
print(type(s1))   

#emepty set
s={}
print(type(s))

#Frozen set immutable 
fs=frozenset(s1)
print(fs)
print(type(fs))

#Dictionary data type= key value pair
d = {'kajal':101,'komal':102,4:'rutuja',5:'priya'}
print(d)
print(type(d))
d[4]='shraddha'
print(d)