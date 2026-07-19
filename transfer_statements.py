'''
for i in range(10):
    if i==5:
        print(i)
        break
    print(i)

cart=[10,20,30,40,50]
for item in cart:
    if item>500:
        print("insurance required")
        break
    print(item)

for i in range(10):
    if i ==7:
        print("insurance required")
        continue
    print(i)

for i in range(10):
    if i%2!=0:
        continue
    print(i)


cart = [10,20,30,500,700,60]
for item in cart:
    if item>500:
        print("can't proceed")
        continue
    print(item)

num=[10,20,0,5,30,0]
for n in num:
    if n==0:
     print("num cannot be divided by 0")
     continue
    print("100/{}={}".format(n,100/n))
    

i=1
while i<=10:
 if i==5:
  continue

 print(i,end=" ")
 i=i+1

i = 1
while i <= 10:
    if i == 5:
        continue

    print(i, end=" ")
    i = i + 1

for x in range(1,50):
    if x%9==0:
        print(x)
    else:
        pass
'''
cart = [10,20,600,30,40,50]
for item in cart:
    if item>=500:
        print("we cannot proceed")
        break
    print(item)
else:
    print("successfully done")