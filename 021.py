class Employee():
    def __init__(self ,name , ename , mhour , year):
        self.name = name
        self.ename = ename
        self.mhour = mhour
        self.year = year

    
    def getYear(self):
        return self.year

    def sethoure (self,newhour):
        self.mhour = newhour

o1 = Employee("food" , 70 , 200 , 1998)
print(o1.getYear)
o1.sethoure("150")
print(o1.price)
        