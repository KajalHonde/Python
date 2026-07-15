'''
#1. print()
print("good mornning")
print()
print("hello")

#2. Seprate
a,b,c =10,20,30
print("values are:",a,b,c)
print("values are:", a,b,c,sep= ",")
print("values are:", a,b,c,sep= " ...")

# 3. END
print("fortune cloud", end=" ")
print("technology")
print("fortune cloud", end=" ")
print("technology")
'''
#Replacement o/p
name="Tom"
age=30
sal=4000
#o/p stom is earning 4000 and his age is 30
print(name,"is earning",sal,"and his age is",age)
print("{}is earning {} and his sal is {}".format(name,sal,age))
print("{x} is earning {y} and his sal is {z}".format (y=sal,z=age,x=name))
print(f"{name}is earning {sal} and his age is {age}")