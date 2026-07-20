
'''
t=(10,20,"python",True)
print(type(t))
print(t)

single valu tuple
t=(10,)
print(type(t))
print(t)

tuple()
l=[10,20,30,"python"]
t=tuple(l)
print(t)
print(type(t))

dynamic input tuple
t=eval(input("Enter list of data"))
print(t)
print(type(t))

len(),min(), max(0, sort()
t=(10,20,10,30,20,40,50)

#functions of tuple

print(len(t))
print(sorted(t))
print(max(t))
print(min(t))
print(sum(t))

#methods of tuple
print(t.count(10))
print(t.index(30))

'''
#tuple packing and unpacking
#packing
# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)
# #unpacking
# t=10,20,30,40,50
# a,b,c,d,e=t
# print("a",a,"\nb",b,"\nc",c,"\nd",d,"\ne",e)

#tuple comprehension
l1=[x for x in range(0,11) if x%2==0]
print(l1)
print(type(l1))