'''
create a set   
empty set
s=set()
print(s)
print(type(s))

intialize
s={10,20,30,"python","java"}
print(s)
print(type(s))

set()  function
l=[10,20,30,40,50,60]
s=set(l)
print(type(s))
print(s)

dynamic input
s=eval(input("enter values"))
print(type(s))
print(s)

built in function of set
1.add
s=set()
s={10,20,30,40}
s.add(120)
print(s)

update
l={10,20,30,40,50,60}
s={1000,200,300}
s.update(l,range(1,5))
print(s)

pop(), remove(), discard(), clear()
l={10,20,30,40,50,60}
s=l.pop()
print(l)
print(s)

remove()
l.remove(10)
print(l)

discard()
l.discard(100)
print(l)

l.clear()
print(l)

# union OR |
s1={10,20,30,40,50}
s2={10,20,30,40}
s3=s1.union(s2)
print(s3)


# intersection OR &
s1={10,20,30,40,50}
s2={10,20,30,40}
s3=s1.intersection(s2)
s3=s1&s2
print(s3)


# difference 
s1={10,20,30,40,50}
s2={10,20,30,40}
# s3=s1.difference(s2)
s3=s1-s2
print(s3)

# symmetric difference
s1={10,20,30,40,50}
s2={10,20,30,40,70}
s3=s1.symmetric_difference(s2)
print(s3)


s1={10,20,30,40,50}
s2={10,20,30,40,90}
s1.symmetric_difference_update(s2)
# s1.difference_update(s2)
# s1.intersection_update(s2)
print(s1)


#isdisjoint
s1={10,20,30}
s2={40,50,60}
print(s1.isdisjoint(s2))


#issubset, issuperset
s1={10,20,30}
s2={40,50,60,10,20,30}

print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s2.issubset(s1))
print(s1.issuperset(s2))

'''
# WRITE A PROGRAM TO ELIMINATE DUPLICATES PRESENT IN THE LIST
l=eval(input("list of values"))
s=set(l)
print(s)