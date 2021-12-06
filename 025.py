listB = [7 , 2 ,3 ,4 ,0]
def findminmax(listA = []):
    listA.sort()
    print(listA[0])
    print(listA[-1])

def findDupl(listB):
    setA = {i for i in listB}
    if setA.__len__() == listB.__len__():  print("yes")
    else: print("no")

findminmax(listB)
findDupl(listB)