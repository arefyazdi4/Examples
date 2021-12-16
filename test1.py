# pass by value or reference
# def func1(b):
#     b.append(4)
#
#
# if __name__ == '__main__':
#     a:list = [1, 2, 3]
#     print(a)
#     func1(a)
#     print(a)

# test str methods
# s1 = "burger"
# s2 = "gay"
#
# # s3=s1.join(["rf","psyco",s2])
# # print(s3)
# a = s1.find("g" , 0 , -1)
# print(a)

# map
# def myfunc(a):
#   return len(a)
#
# x = map(myfunc, ('apple', 'banana', 'cherry'))
#
# print("\n\n",x)
#
# #convert the map into a list, for readability:
# print(list(x))
#
# print("****************1**************")
# #################
# list1 = [1 , 2 , 3]
#
# for item in map(myfunc, ('apple', 'banana', 'cherry')): print(item)
#
# print("****************2**************")
# for item in x: print(item)
#
# for item in map(lambda n : n**2 , list1): print(item)
# for item in map(lambda n : n**2 , [1 , 2 , 3]): print(item)
#
# print("****************3**************")
#
# x2 = filter(myfunc, ('apple', 'banana', 'cherry'))
# print(x2)
# print(list(x2))
#
# for item in filter(myfunc, ('apple', 'banana', 'cherry')): print(item)
# for item in filter(lambda n : n<3 , list1): print(item)

# test print
# print("hi","hello" ,end = '   *')
# print("End line")


# if __name__ == '__main__':
#     listB = [7, 2, 3, 4, 0]
#
#
#     def findminmax(listA=[]):
#         listA.sort()
#         print(listA[0])
#         print(listA[-1])
#
#
#     def findDupl(listB):
#         setA = {i for i in listB}
#         if setA.__len__() == listB.__len__():
#             print("yes")
#         else:
#             print("no")
#
#
#     findminmax(listB)
#     findDupl(listB)
