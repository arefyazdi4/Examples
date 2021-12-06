class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        node.next = self.head
        if self.head:
            current = self.head
            for i in range(self.size-1):
                current = current.next
            current.next = node
        else:
            self.head = node
        self.size += 1

    def delete(self, data):
        current = self.head
        cheek_remove = True
        for i in range(self.size):
            if data == self.head.data:
                self.head = self.head.next
            if data == current.data:
                temp = current.next
                for j in range(self.size-1):
                    current = current.next
                current.next = temp
                self.size -= 1
                cheek_remove = False
                break
            else:
                current = current.next
        if cheek_remove:
            print("data not found")

    def generate(self):
        current = self.head
        for i in range(self.size):
            yield current.data
            current = current.next


if __name__ == '__main__':

    num = CircularList()
    num.append(1)
    num.append(2)
    num.append(3)
    num.append(4)
    num.append(5)
    num.append(6)
    num.append(7)

    print("hole data")
    for i in num.generate():
        print(i)

    print("remove first node")
    num.delete(1)
    for i in num.generate():
        print(i)

    print("remove node in the middle")
    num.delete(4)
    for i in num.generate():
        print(i)

    print("remove last node")
    num.delete(7)
    for i in num.generate():
        print(i)

    print("in case dataa doesn't exist")
    num.delete(10)