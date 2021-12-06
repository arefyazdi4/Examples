def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print("\n\n",x)

#convert the map into a list, for readability:
print(list(x))

print("****************1**************")
#################
list1 = [1 , 2 , 3]

for item in map(myfunc, ('apple', 'banana', 'cherry')): print(item)

print("****************2**************")
for item in x: print(item)

for item in map(lambda n : n**2 , list1): print(item)
for item in map(lambda n : n**2 , [1 , 2 , 3]): print(item)

print("****************3**************")

x2 = filter(myfunc, ('apple', 'banana', 'cherry'))
print(x2)
print(list(x2))

for item in filter(myfunc, ('apple', 'banana', 'cherry')): print(item)
for item in filter(lambda n : n<3 , list1): print(item)