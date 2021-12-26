from stackClass import Stack


class Rpn:
    @staticmethod
    def operator_applier(operator, *args):
        if operator == '+':
            result = 0
            for num in args:
                result = result + num
            return result
        elif operator == '*':
            result = 1
            for num in args:
                result = result * num
            return result
        elif operator == '-':
            result = args[0]
            for num in args[1:]:
                result = result - num
            return result
        elif operator == '/':
            result = args[0]
            for num in args[1:]:
                result = result / num
            return result

    @staticmethod
    def reverse_p_notation(arithmetic_expression: Stack):
        root_node = arithmetic_expression.pop()
        if root_node in ('+', '*', '-', '/'):
            right_node = Rpn.reverse_p_notation(arithmetic_expression)
            left_node = Rpn.reverse_p_notation(arithmetic_expression)
            return Rpn.operator_applier(root_node, left_node, right_node)
        else:
            return int(root_node)


if __name__ == '__main__':
    statements_list = '5 4 + 5 3 - *'.split()
    statements_stack = Stack()
    for statement in statements_list:
        statements_stack.push(statement)

    print(Rpn.reverse_p_notation(statements_stack))
