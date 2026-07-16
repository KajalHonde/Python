'''
i =0
while i<5:
  print("hello")
  i=i+1

#print 1 t0 10
i =1
while i<11:
  print(i)
  i=i+1
  

#Accept a number and print its table
n = int(input())
i=1
while i<11:
  print(n ,"*" ,i,"=",n*i)
  i=i+1

#Accept a number and print its reverse
n = int(input())
rev=0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
    
print(rev)

 
i=0
j=0
for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()
        
   '''
     
 
i=1
j=1

for i in range(1,4):
    for j in range(1,i+1):
        print(j," ",end="")
        
        
    print()
    
    