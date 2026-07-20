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
 '''
 
#create a list of even num from 1 to 100 
#which are divisible by 7

li=[]
for i in range(1,100):
  if(i%2==0) and (i%7==0):
       li.append(i)
print(li)