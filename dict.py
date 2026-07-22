# empty dict
'''
d={}
print(d)
print(type(d))


# B intialization
d={1:"python",2:"java",3:"c++"}
print(d)
print(d[1])
print(type(d))

# dynamic dict
d=eval(input("enter data:"))
print(type(d))
print(d)


# dict()
d=dict([(1,"tom"),(2,"jack")])
print(type(d))
print(d)

# e
d={"name":["kajal","komal","priya"],"age":[10,30,40]}
print(d)
print(type(d))

# Adding values in dict
d={1:"kajal"}
d[2]="java"
print(d)
d[2]="DS"
print(d)

for x in d:
    print(d)
    

# deletinng
d={"name":["kajal","komal","priya"],"age":[10,30,40]}
print(len(d))
print(d)
del d["name"]
print(d)
print(type(d))
for x in d :
    print(x)

# get(key)
d={1:"kajal",2:"komal",3:"priya",4:"shraddha",5:"gauri"}
print(d.get(1))
d[3]="sayali"
print(d)
print(d.get(6))
print(d.get(6,"rutuja"))

# pop(), popitem()
d={1:"kajal",2:"komal",3:"priya",4:"shraddha",5:"gauri"}
print(d)
d.pop(3)
print(d)
d.popitem()
print(d)

# keys(), values(), items()
d={1:"kajal",2:"komal",3:"priya",4:"shraddha",5:"gauri"}
print(d.keys())
print(d.values())
print(d.items())

v=d.values()
print(v)
for k in v:
    print(v)
    
v=d.items()
print(v)
for k in v:
    print(v)

#copy()
d={1:"kajal",2:"komal",3:"priya",4:"shraddha",5:"gauri"}
d2=d.copy()
print(d2)
print(d)
d[4]="DS"
print(d)
print(d2)
    

# update
d={1:"kajal",2:"komal",3:"priya",4:"shraddha",5:"gauri"}
d2={6:"sakshi",7:"apurva"}
d.update(d2)
print(d)
'''
# dictionary comprehension
d={x*x for x in range(1,6)}
print(d)
print(type(d))