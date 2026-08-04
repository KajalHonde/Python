'''
f=open("Files.txt",'w')
print("filename",f.name)
print("filemode",f.mode)
print("is file readable",f.readable())
print("Is file writeable",f.writable())
print("is file close",f.closed)
f.close()
print("Is file  closed",f.closed)
f.close()


f=open("Files.txt",'w')
f.write("Hello world\n")
f.write("You are a good person")
'
# WRITE MODE

l=["python ","java ","c++ "]
f=open("Files.txt","w")
f.writelines(l)
f.close()

# a.write(str)
f=open("Files.txt","w")
f.write("Hello world\n")
f.write("You are good\n")
f.write("bye\n")
f.close()


f=open("Files.txt","a")
f.write("You are in append mode")
f.close()

# reading data from the text file
f=open("Files.txt",'r')
data=f.read()
data=f.read(7)
print(data)

data=f.readline()
print(data)
print(type(data))

data=f.readlines()
print(data)
print(type(data))

print(f.read())
print(type(f.read))
for line in f:
    print(line)


# WITH STATEMENT

with open("Files.txt","r") as f:
    data=f.read()
    print(data)
    print("Is file Closed",f.closed)    

print("Is file Closed",f.closed)  

f=open("Files.txt",'r')
print(f.tell())
f.seek(5)
print(f.tell())
data=f.read(6)

'''
f=open("Files.txt","w+")
f.write("Kajal")
print(f.tell())
f.seek(0)
data=f.read()
print(data)
f.close()