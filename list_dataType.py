#List --mutable
'''
a=[10,20,"python",True]
print(a[2])
a.append("hello")
print(a)
a.remove(True)

print(a)
print(type(a))


#dynammic list
l1=eval(input("enter list of data"))
print(l1)
print(type(l1))


#intialization of list
l1=[10,20,"python","java",True,10]
print(l1)
print(type(l1))

#creating list --mutable
l1=[]
print(l1)
print(type(l1))

#list()
l1=list(range(1,11))
print(l1)
print(type(l1))

#split
s="python is very easy"
l=s.split()
print(l)
print(type(l))


#accessing list elements
l1=[10,20,30,"python","java",True,50]
print(l1)
print(l1[3])
#print(l1[20])
print(l1[-5])
print(l1[2:20])
print(l1[1:5:-1])
print(l1[10:5:-1])
print(l1[-1:-5:-1])

#traverse of list
l1=[10,20,30,40,"python","tom",True,60]
for x in l1:
    print(x)
   

l1=[10,20,30,40,50,60,70]
i=0
while i<len(l1):
    print(l1[i])
    i=i+1

 #count
l1=[1,2,3,1,1,1,4,4,4,5,5,5,5,5,5] 
print(l1.count(2)) 

#index
print(l1.index(5))

#append
l1.append(10)
l1[1]=100
print(l1)
 
 
#create a list of even num from 1 to 100 
#which are divisible by 7

li=[]
for i in range(1,100):
  if(i%2==0) and (i%7==0):
       li.append(i)
print(li)

#insert
s=[10,20,30,40,50,60]
s.insert(2,300)
print(s)
s.insert(20,400)
print(s)

s.insert(-2,4)
print(s)


#extend()
l1=["python","java","c"]
l2=["ruby","c++","html","css"]
l1.extend(l2)
s=["hello"]
l1.extend(s)
print("enter names of programming languages",l1)

#remove(), po(), clear()

s=[10,20,30,40,50,60,70,80,90]
del s
print(s)

s.pop()
print(s)

s.remove(30)
print(s)

s.clear()
print(s)

#reverse()
s=[10,20,30,40,50,60,70,80]
s.reverse()
print(s)

n=[2,4,6,1,0,7,9]
n.sort(reverse=True)
print(n)

#Aliasing and cloning

s=[10,20,30,40,50]
s1=s
print(s1)
print(id(s))
print(id(s1))

s1=s[:]
s1=s.copy()
print(s1)
print(id(s))
print(id(s1))


#concatetion(+) and repetation(*)
l=[10,20]
l1=[30,40]
l2=l+l1
print(l2)

s=[10,20,30,40]
print(s*3)


#comparison (<, <=, >=, >, ==)
# l1=[10,20,30,40,50]
# l2=[60,70]
# print(l1<l2)

# s=["python","java"]
# s1=["python","java"]

#tuple is immutable

s=("python","java")
s1=("python","java")
print(s1 is s)


#membership operator
k=[10,20,30,40,50,60,70]
print(100 in k)
print(10 in k)
print(100 not in k)

#nested list
s=[10,20,30,40,50,[70,80]]
print(s)
print(s[5][0])
print(s[3])


list comprension

normal way
l=[]
for i in range(1,6):
    l.append(i)
print(l)

#list comprension way:
l=[i for i in range(1,6)]
print(l)


l=[2,4,6,8,10]
l2=[x*x for x in l]
print(l2)

'''
l=[2,4,6,8,11,13,17,10]
l2=[i for i in l if i%2==0]
print(l2)