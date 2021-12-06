class Node:
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


def check_brackets(statement):
    stack = Stack()

    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        if ch in ('}', ']', ')'):
            last = stack.pop()
            if last == '{' and ch == '}':
                continue
            elif last == '[' and ch == ']':
                continue
            elif last == '(' and ch == ')':
                continue
            else:
                return False
    if stack.size > 0:
        return False
    else:
        return True


if __name__ == '__main__':

    statements = (
        "{(foo) (bar)} [hello] (((this)is)a)test",
        "{(foo) (bar)} [hello] (((this)is))a test",
        "{(foo) (bar)} [hello] (((this)is)a)test))")

    for statement in statements:
        result = check_brackets(statement)
        print(f'{statement} -->{result}')
