from time import sleep
import os


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def iter(self):
        current_node = self.top
        while current_node:
            data_val = current_node.data
            current_node = current_node.next
            yield data_val


class Map:
    def __init__(self):
        # map is 2D matrix contains our elements
        # 9 is wall
        # 0 is empty space
        # 5 is carrot
        # and other number show were rabbit is taking us to
        self.map = [[9, 9, 9, 9, 9, 9, 9],
                    [9, 0, 0, 0, 0, 9, 9],
                    [9, 0, 0, 9, 0, 9, 9],
                    [9, 0, 0, 0, 9, 0, 9],
                    [9, 0, 9, 9, 0, 0, 9],
                    [9, 0, 0, 0, 0, 5, 9],
                    [9, 9, 9, 9, 9, 9, 9]
                    ]

        self.show()
        self.road = Stack()  # memorise the coordinate of each path that rabbit goes
        step = 0  # counter the number of every step that we take
        (i, j) = 1, 0  # start point (where rabbit stand at the beginning)
        # i and j present where rabbit is at the moment

        while self.map[i][j] != 5 + 1:  # loop stop when we reach to the carrot value 5 mean it
            # this condition check the space around rabbit to find free space to go
            if self.map[i][j + 1] in (0, 5):  # right
                (i, j) = i, j + 1  # update were rabbit stand now
                self.map[i][j] += 1  # modify the space value to show how many time we passes here
                step += 1  # one more step is taken
                print('step: ', step)
                self.show()  # print the map to see how things is going on
                self.road.push((i, j))
            elif self.map[i + 1][j] in (0, 5):  # down
                (i, j) = i + 1, j
                self.map[i][j] += 1
                step += 1
                print('step: ', step)
                self.show()
                self.road.push((i, j))
            elif self.map[i - 1][j] in (0, 5):  # up
                (i, j) = i - 1, j
                self.map[i][j] += 1
                step += 1
                print('step: ', step)
                self.show()
                self.road.push((i, j))
            elif self.map[i][j - 1] in (0, 5):  # left
                (i, j) = i, j - 1
                self.map[i][j] += 1
                step += 1
                print('step: ', step)
                self.show()
                self.road.push((i, j))
            else:  # in case that we are dead end, and need to turn back were we came
                self.map[i][j] += 1  # modify the space value to show how many time we passes here
                self.road.pop()  # remove current coordinate from road slut
                (i, j) = self.road.peek()  # put the rabbit in the last place we were
                step += 1
                print('step: ', step)
                self.show()
        print("\n\n**********************")
        print('rabbit reached the carrot')
        print("**********************")

    def show(self):
        os.system('Cls')
        for x in range(len(self.map)):
            print(self.map[x])
        sleep(0.5)


if __name__ == '__main__':
    obj1 = Map()
