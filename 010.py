listA = [1,2,3]
tupleA= (4,5,6)

print(type(listA))
print(type(tupleA))

print(2*listA)
print(2*tupleA)

listB = [7]
tupleB = (8)
tupleC = (9,)
print(type(listB))
print(type(tupleB))
print(type(tupleC))

tupleD = tupleA+tupleC
tupleE = tupleA,tupleC
print(tupleD)
print(tupleE)

print(tupleA.index(4))
print(tupleA.count(4))
print(4 in tupleA)

first,second,thierd = tupleA
print(first)
print("/////////////////////////////////////")
dicA={}
dicB = {1:"a",2:"b",3:"c"}
for i in dicB:
    print(i , dicB[i])

print("/////////////////////////////////////")
strA = "hello mr burger"
strB = strA.split()
print(strA)
print(strB)
strC = strA.replace(" " , "A")
print(strA)
print(strC)
listC = list(strA)
print(listC)