from collections import deque
import time


class ListQueue:
    def __init__(self):
        self.item = deque([])
        self.size = 0

    def enqueue(self, data):
        self.item.append(data)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.item.popleft()

    def __iter__(self):
        for data in self.item:
            yield data


class Node:
    def __init__(self, data, nextData=None, prevData=None):
        self.data = data
        self.next = nextData
        self.prev = prevData


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.head:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.size += 1

    def dequeue(self):
        if self.head:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = Node
            else:
                self.head = None
                self.tail = None
            self.size -= 0


if __name__ == '__main__':

    print("///////////////////////////")
    a = ListQueue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
    for i in a:
        print(i)
    print(a.item)
    print(a.dequeue())
    print(a.size)
    print(a.item)
    print("///////////////////////////")
    b = Queue()
    b.enqueue(5)
    b.enqueue(6)
    b.enqueue(7)
    b.enqueue(8)
    b.dequeue()
    print(b.size)
    print("///////////////////////////")
    for i in range(10000):
        a.enqueue(1)
    t = time.time()
    for i in range(10000):
        a.dequeue()
    print(time.time() - t)

    for i in range(10000):
        b.enqueue(1)
    t = time.time()
    for i in range(10000):
        b.dequeue()
    print(time.time() - t)
    print("///////////////////////////")
