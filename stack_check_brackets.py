class Node():
    def __init__(self, data=""):
        self.data = data
        self.next = None
        self.preview = None


class Stack:
    def __init__(self):
        self.top: Node = None
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


def checkBrackets(statement):
    stack = Stack()
    openBrackets = ('(', '[', '{')
    closeBrackets = (')', ']', '}')
    for ch in statement:
        if ch in openBrackets:
            stack.push(ch)
        if ch in closeBrackets:
            last = stack.pop()
            if ch == ')' and last == '(':
                continue
            elif ch == '}' and last == '{':
                continue
            elif ch == ']' and last == '[':
                continue
            else:
                return False
    if stack.size > 0:
        return False
    else:
        return True


print("////////////////////////////")
print(checkBrackets("{34-(2)r}+1[]"))  # true
print(checkBrackets("(]*{34-(2)r}+1[]"))  # false
print(checkBrackets("*{34-(2)r}+1[]("))  # false
print("////////////////////////////")
