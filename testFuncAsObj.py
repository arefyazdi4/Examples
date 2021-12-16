


def Unitconvert (unittype , value):

    value = abs(value)

    ItoC = lambda n : n*2.5
    CtoI = lambda n : n/2.5

    if (unittype == "cent"):
        print("Your Lenght is ",list(map(CtoI , [value])),"long in inch Unit")

        print("Let see how long it would be")
        if(checkanswer()):
            print ("our size in centimeter")
            howlongis(cent , value)

    elif(unittype == "inch"):
        print("Your Lenght is ",ItoC(value),"long in inch Unit")

        print ("Let see how long it would be")
        if(checkanswer()):
            print ("our size in inche")
            howlongis(inch , value)

    else: print("invalied Unit!")




def howlongis (unit , lenght):
    long = ""
    print ("|"+long.join(unit(lenght))+">")


def cent(lenght):
    size = "======"
    return  [size for i in range(lenght)]
    

def inch(lenght):
    size = "==============="
    return  [size for i in range(lenght)]


def checkanswer():
    print("Y for agree and N for disagree")
    answer = input()
    answer = answer.casefold()

    if (answer[0] == "y"):
        return True
    else: return False

print("\n\n-------------6 centimeter----------\n")
Unitconvert("cent" , 6)
print("\n\n-------------3 inches-----------\n")
Unitconvert("inch" , 3)
