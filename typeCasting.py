
# converting float into integer
x = 10.35
print(x)
print(type(x))
y=int(x)
print(y)
print(type(y))
print(x)
print(type(x))

# bool into integer
a = 10.45

a= True
print(a)
print(type(a))

#string into int

e= "10"
d= "20"
f= int(e)+int(d)
print(f)

#float

x = 12   #int to float
i = False #bool to float
p = "34" #str to float
l = 2+5j #error its complex datatype
k=float(x)
print(type(k))

f=float(i)
print(type(f))

c=float(p)
print(type(c))

# will not execute because complex is not allowed
h= float(l)
print(type(h))


# othr data typ3e into complex

x = "12"  #string
y= (complex(x))
print(y)

w=3 #integer
t= True  # bool
print(complex(w))
print(complex(t))

x=False
y=True
z= complex(x,y)
print(z)

#other datatype into boolean

x = 1 # int to bool 
z = bool(x)
print(z)

y = 0.0  # float to bool 
h = bool(y)
print(h)

f = "ab"  # string to bool 
k = bool(f)
print(k)

v = 0.0+1j
t = bool(v)
print(t)



#other data type into string
x=14 #int to string
y=13
z= str(x+y)
print(type(z))

t = 0.2
r=str(t)
print(type(r))
 

