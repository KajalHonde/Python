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
    
'''
# deletinng
d={"name":["kajal","komal","priya"],"age":[10,30,40]}
print(len(d))
print(d)
del d["name"]
print(d)
print(type(d))
for x in d :
    print(x)