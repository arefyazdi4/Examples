class Node(object):

    def __init__(self, data="", nextAddress=None, previewAddress=None):
        self.data = data
        self.next = nextAddress
        self.preview = previewAddress


class CircularDoubleLinklist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def __iter__(self):
        currentNode = self.head
        count = self.counter
        while (count != 0):
            count -= 1
            dataVal = currentNode.data
            currentNode = currentNode.next
            yield dataVal

    def apend(self, data):
        newNode = Node(data)
        self.counter += 1
        if self.head:
            self.tail.next = newNode
            newNode.preview = self.tail
            newNode.next = self.head
            self.tail = newNode
            self.head.preview = self.tail
        else:
            self.head = newNode
            self.tail = newNode
            self.head.next = newNode
            self.head.preview = newNode
