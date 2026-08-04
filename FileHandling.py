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

f=open("Files.txt","w+")
f.write("Kajal")
print(f.tell())
f.seek(0)
data=f.read()
print(data)
f.close()


import os
fname="c\\Files.txt"
if os.path.isfile(fname):
    f=open(fname,"r")
    data=f.read()
    print(data)
    f.close()
else:
    print("File not found")
    

import os
fname=input("Enter file name")
if os.path.isfile(fname):
    print("file with name",fname,"exists")
    f=open(fname,'r')

    lcount=wcount=ccount=0
    for line in f:
        lcount=lcount+1
        ccount=ccount+len(line)
        words=line.split()
        wcount=wcount+len(words)
        
        print("no of lines:",lcount)
        print("no of words:",wcount)
        print("no of chars:",ccount)
else:
    print("File doesn't exists")
    

# Reading and writting binary File
f1=open("background.jpg.","rb")
f2=open("background.jpg.","wb")
data=f1.read()
f2.write(data)
f1.close()
f2.close()

'''
# list of numbers 


l = [10, 15, 22, 35, 40, 51, 68, 79]

fe = open("even.txt", "w")
fo = open("odd.txt", "w")

for i in l:
    if i % 2 == 0:
        fe.write(str(i) + "\n")
    else:
        fo.write(str(i) + "\n")

fe.close()
fo.close()

print("Data Written Successfully")