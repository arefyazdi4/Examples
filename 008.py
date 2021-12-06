def threeRoot(m):
    m -= m%3
    while(m != 0):
        yield m
        m -= 3

def threeRootList(n):
    n -= n%3
    lst = []
    while(n != 0):
        lst.append(n)
        n -= 3
    return lst

lst1 = [4,3,1,5,2]
#lst2 = sorted(lst1)
gen1 = (i for i in lst1)
print(gen1)
#lisgen = list(gen1)
lisgen = [j for j in gen1]
for i in sorted(lisgen):print(i)

def numberGenerator(n):
     number = 0
     while number < n:
         yield number
         number += 1

# g = numberGenerator(10000000000)
# counter = 0
# while counter < 10000000000:
#     print(next(g))
#     counter += 1

 #################################   
def myGenerator1(n):
    for i in range(n):
        yield i

def myGenerator2(n, m):
    for j in range(n, m):
        yield j

def myGenerator3(n, m):
    yield from myGenerator1(n)
    yield from myGenerator2(n, m)
    yield from myGenerator2(m, m*2)

print(list(myGenerator1(5)))
print(list(myGenerator2(5, 10)))
print(list(myGenerator3(0, 10)))
###########################################