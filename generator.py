# Generator
'''
l1=(x*x for x in  range[10000000000])
print(l1[2]) #error


g=(x*x for x in  range(10000000000))
print(type(g))
print(next(g))


def mygen():
    yield 'A'
    yield 'B'
    yield 'c'
    yield 'd'
    yield 'e'
    yield 'f'
    yield 'g'
    yield 'h'

g=mygen() 
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

'''
def countdown(num):
    print("start countdown")
    while(num>0):
        yield num
        num=num-1
        

values=countdown(5)
for x in values:
    print(x)
