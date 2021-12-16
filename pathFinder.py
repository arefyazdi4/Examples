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

    def __iter__(self):
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
                    print('β', end='')
                elif self.map[i][j] == -2:
                    print('⇩', end='')
                elif self.map[i][j] == -3:
                    print('⇨', end='')
                elif self.map[i][j] == -4:
                    print('⇫', end='')
                elif self.map[i][j] == -5:
                    print('⇦', end='')
                elif self.map[i][j] == -6:
                    print('⁕', end='')
            print()
        time.sleep(0.3)

    def wall_maker(self):
        # cleaning it up
        self.map = [[0 for j in range(self.width)] for i in range(self.height)]
        # build out side walls
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                    self.map[i][j] = -1

        # appending blocks to map
        if self.wall:
            for point in self.wall:
                self.map[point[0]][point[1]] = -1
        self.map[1][1] = 1  # set start point
        self.map[self.height - 2][self.width - 2] = 2  # set end point

    def move(self, step: int, i=0, j=0, dx=0, dy=0):
        self.map[i][j] = step
        self.print_map()
        self.path.push(step)
        self.path_finder(i + dx, j + dy)

    def path_finder(self, head_i=1, head_j=1):
        if self.map[head_i][head_j] == 2:
            exit()
        else:
            if self.map[head_i][head_j + 1] >= 0:
                self.move(-3, head_i, head_j, dy=1)  # Right
            if self.map[head_i + 1][head_j] >= 0:
                self.move(-2, head_i, head_j, dx=1)  # Down
            if self.map[head_i - 1][head_j] >= 0:
                self.move(-4, head_i, head_j, dx=-1)  # Up
            if self.map[head_i][head_j - 1] >= 0:
                self.move(-5, head_i, head_j, dy=-1)  # Left
            # wrong way step back
            self.path.pop()
            self.map[head_i][head_j] = -6  # change this for marking wrong path
            self.print_map()


if __name__ == '__main__':
    print("///////first first_maze///////")
    first_maze = Maze(10, 20)
    for i in (3, 4, 5, 6, 7, 8):
        first_maze.wall.append([i, 14])
    for j in (9, 10, 11, 12, 13, 14):
        first_maze.wall.append([3, j])
    first_maze.wall.append([4, 9])
    for i in (1, 2, 3, 4, 5, 6):
        first_maze.wall.append([i, 6])
    for j in (6, 7, 8, 9, 10, 11):
        first_maze.wall.append([6, j])
    first_maze.wall.append([5, 11])
    first_maze.wall.append([7, 5])
    first_maze.wall.append([2, 15])

    first_maze.wall_maker()
    # first_maze.print_map()
    # input("press any key to contain...")
    # first_maze.path_finder()

    print("///////second first_maze///////")
    second_maze = Maze(8, 17)
    for j in (13, 14, 15):
        for i in (1, 2, 3, 4):
            second_maze.wall.append([i, j])
    for j in (10, 11, 12):
        second_maze.wall.append([3, j])
        second_maze.wall.append([4, j])
    for j in (7, 8, 9):
        second_maze.wall.append([2, j])
        second_maze.wall.append([5, j])
    for j in (4, 5, 6):
        second_maze.wall.append([3, j])

    second_maze.wall_maker()
    second_maze.print_map()
    input("press any key to contain...")
    second_maze.path_finder()

