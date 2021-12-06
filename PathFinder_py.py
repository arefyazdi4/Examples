import time
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
        self.size += 1
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

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


class Maze:
    def __init__(self, height: int, width: int):
        self.map = [[0 for j in range(width)] for i in range(height)]
        self.height = height
        self.width = width
        self.path = Stack()
        self.wall = []
        self.starTime = time.time()
        self.endTime = time.time()

    def print_map(self):
        os.system('Cls')
        for i in range(self.height):
            for j in range(self.width):
                if self.map[i][j] == 0:
                    print(' ', end='')
                elif self.map[i][j] == -1:
                    print('■', end='')
                elif self.map[i][j] == 1:
                    print('⨀', end='')
                elif self.map[i][j] == 2:
                    print('β ', end='')
                elif self.map[i][j] == -2:
                    print('⇩', end='')
                elif self.map[i][j] == -3:
                    print('⇒', end='')
                elif self.map[i][j] == -4:
                    print('⇑', end='')
                elif self.map[i][j] == -5:
                    print('⇐', end='')

            print()
        time.sleep(0.3)

    def print_path(self):
        self.wall_maker()
        # making route according to path Stack
        headi, headj = self.height - 2, self.width - 2
        for path in self.path.iter():
            if path == "Down":
                headi -= 1
            elif path == "Right":
                headj -= 1
            elif path == "Up":
                headi += 1
            elif path == "Left":
                headj += 1
            self.map[headi][headj] = -2
            self.print_map()

        self.map[1][1] = 1  # set start point
        self.print_map()
        print("Path length from point A to point B:  ", self.path.size, "  pixls")
        self.run_time()

    def wall_maker(self):

        # cleaning it up
        self.map = [[0 for j in range(self.width)] for i in range(self.height)]

        # build out side walls
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                    self.map[i][j] = -1

        # appending blockes to map
        if self.wall:
            for point in self.wall:
                self.map[point[0]][point[1]] = -1

        self.map[1][1] = 1  # set start point
        self.map[self.height - 2][self.width - 2] = 2  # set end point

    def run_time(self):
        t3 = self.endTime - self.starTime
        milisec = ((t3 % 1) * 100) // 1
        sec = (t3 % 60) // 1
        mint = (t3 // 60) % 60
        hour = (mint // 60)
        print("Solve time is ==>", "min:", int(mint), "    s:", int(sec), "     ms:", int(milisec))

    def move(self, step: int, i=0, j=0, dx=0, dy=0):
        self.map[i][j] = step
        self.print_map()
        self.path.push(step)
        self.path_finder(i + dx, j + dy)

    def path_finder(self, headi=1, headj=1):
        if self.map[headi][headj] == 2:
            print("Find it****************")
            self.map[1][1] = 1  # set start point
            self.print_map()
            # self.endTime = time.time()
            # input("press any key to contain...")
            # self.printPath()
            exit()
        else:
            if self.map[headi + 1][headj] >= 0:
                self.move(-2, headi, headj, dx=1)  # Down
            if self.map[headi][headj + 1] >= 0:
                self.move(-3, headi, headj, dy=1)  # Right
            if self.map[headi - 1][headj] >= 0:
                self.move(-4, headi, headj, dx=-1)  # Up
            if self.map[headi][headj - 1] >= 0:
                self.move(-5, headi, headj, dy=-1)  # Left

            self.print_map()
            self.path.pop()
            self.map[headi][headj] = 0


if __name__ == '__main__':
    print("///////////////////////////")
    maze = Maze(10, 20)

    for i in (3, 4, 5, 6, 7, 8):
        maze.wall.append([i, 14])
    for j in (9, 10, 11, 12, 13, 14):
        maze.wall.append([3, j])
    maze.wall.append([4, 9])
    for i in (1, 2, 3, 4, 5, 6):
        maze.wall.append([i, 6])
    for j in (6, 7, 8, 9, 10, 11):
        maze.wall.append([6, j])
    maze.wall.append([5, 11])
    maze.wall.append([7, 5])
    maze.wall.append([2, 15])

    maze.wall_maker()
    maze.print_map()

    input("press any key to contain...")
    maze.path_finder()
