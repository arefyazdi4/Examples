class ContactInfo (object):

    def __init__ (self , data = "" , nextAddress = None , previewAddress = None):
        self.data = data
        self.next = nextAddress
        self.preview = previewAddress
        print("contact class created")

    def __del__(self):
        print("contact class Deleted")

    @classmethod

    def getObjectAddress (cls):
        return cls  
        
    def showContactInfo(self):
        print ("Contact info:\n" , "    name: " , end = "")
        if (self.data != ""):
            print(self.data)
        else : print("none initioalized")
    
    def creatContect(self):
        pass

    
   

class ContactInfoProvider (ContactInfo):

    def __init__(self, data="", nextAddress=None ,previewAddress = None):
        super().__init__( data = data , nextAddress=nextAddress , previewAddress = None)
        self.newContact = None
        print("ContactInfoProvider created")  



    def __del__(self):
        return super().__del__()
        print("ContactInfoProvider deleted")
            

    # def creatContect(self , newData):
    #     lastContact:ContactInfoProvider = self
    #     while lastContact.nextContact:
    #         lastContact = lastContact.nextContact
    #     lastContact.nextContact = ContactInfoProvider(newData)
        

class BasicInfoProvider():
    
    def __init__(self):
        print("BasicInfoProvide created")
        self.head:ContactInfoProvider = None
        self.tail:ContactInfoProvider = None
        self.counter = 0

    def __del__(self):
        print("basicInfoProvuder deleted")

    def iter(self):
        currentNode = self.head
        while currentNode:
            dataVal = currentNode.data
            currentNode=currentNode.next
            yield dataVal
    
    def serchData(self , data ,direct = "head2tail"):
        if (direct == "head2tail"):
            currentNode = self.head
            while currentNode:
                if(currentNode.data == data ):
                    return currentNode
                currentNode = currentNode.next
            return None
        elif(direct == "tail2head"):
            currentNode = self.tail
            while currentNode:
                if(currentNode.data == data ):
                    return currentNode
                currentNode = currentNode.preview
            return None
        else:
            print("wrong inpt directio")

    def apend(self ,data):
        newNode = ContactInfoProvider(data)
        self.counter += 1
        if self.head :
            self.tail.next = newNode
            newNode.preview = self.tail
            self.tail = newNode
        else :
            self.head = newNode 
            self.tail = newNode
    
    def removeNode(self , data):
        node = self.serchData(data)
        if(node):
            self.counter -= 1
            if ((node != self.tail) and (node != self.head)):
                node.preview.next = node.next
                node.next.preview = node.preview
            else:
                if (node == self.tail):
                    self.tail = node.preview
                    self.tail.next = None
                else:
                    self.head = node.next
                    self.head.preview = None      
        else:
            print("data dsoen't exist")

    def displayAll(self):
        contact = self.head
        while contact:
            contact.showContactInfo()
            contact = contact.next

    def findMax(self):
        node:ContactInfoProvider = self.head
        max = int(node.data)
        while node:
            if(int(node.data) > max ):
                max = int(node.data)
            node = node.next
        return max

    def findMin(self):
        node:ContactInfoProvider = self.head
        min = int(node.data)
        while node:
            if(int(node.data) < min ):
                min = int(node.data)
            node = node.next
        return min

    def findMean(self):
        node:ContactInfoProvider = self.head
        sum = 0
        while node:
            sum += int(node.data)
            node = node.next
        return sum/self.counter

    
    

    
def main():
    basicInfo = BasicInfoProvider()
    basicInfo.apend("1")
    basicInfo.apend("2")
    basicInfo.apend("3")
    basicInfo.apend("4")
    basicInfo.apend("5")
    basicInfo.apend("6")
    basicInfo.apend("7")

    print("/////////////////////////////////")
    basicInfo.head.showContactInfo()
    basicInfo.tail.showContactInfo()
    print("/////////////////////////////////")
    basicInfo.removeNode("7")
    basicInfo.tail.showContactInfo()
    print("/////////////////////////////////")
    basicInfo.tail.preview.showContactInfo()
    print(basicInfo.tail.next)
    print("/////////////////////////////////")
    basicInfo.displayAll()
    print("/////////////////////////////////")
    print("max number is: " , basicInfo.findMax())
    print("min number is: " , basicInfo.findMin())
    print("mean number is: " , basicInfo.findMean())
    print("/////////////////////////////////###**##*")
    basicInfo.serchData("4").showContactInfo()
    basicInfo.serchData("4" , "tail2head").next.showContactInfo()
    basicInfo.serchData("4" , "head2tail").preview.showContactInfo()
    print("/////////////////////////////////")
    print(basicInfo.serchData("0"))
    basicInfo.serchData("2" , "start2end")
    print("/////////////////////////////////")
    for i in basicInfo.iter():
        print(i)
    print("/////////////////////////////////")
    basicInfo.removeNode("0")
    basicInfo.removeNode("4")
    basicInfo.serchData("3").next.showContactInfo()
    basicInfo.serchData("5").preview.showContactInfo()
    print("/////////////////////////////////")


if __name__ == "__main__":
    main()

