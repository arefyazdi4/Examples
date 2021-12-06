class doubleLink ():
    def print10(self , num = 10):
        current = self.head
        for i in range(num):
            print(current.data)
            current = current.next
        
        current = current.preview
        while current:
            print(current.data)
            current = current.preview
        

