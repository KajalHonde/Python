# handling zip file
'''
from zipfile import*
f=ZipFile("The Zip Filezip.zip","w",ZIP_DEFLATED)
f.write("tuple.py")
f.write("Files.txt")
f.write("lambda.py")
f.close()
'''
from zipfile import *
f=ZipFile("The Zip Filezip.zip","r",ZIP_DEFLATED)
files=f.namelist()
print(files)
print(type(files))
f1=open(files[0],"r")
data=f1.read()
print(data)
f1.close()
f.close()