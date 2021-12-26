from stackClass import Stack


class Rpn:
    @staticmethod
    def __operator_applier(operator, *args):
        if operator == '+':
            result = 0
            for num in args:
                result += num
            return result
        elif operator == '*':
            result = 1
            for num in args:
                result *= num
            return result
        elif operator == '-':
            result = args[0]
            for num in args[1:]:
                result -= num
            return result
        elif operator == '/':
            result = args[0]
            for num in args[1:]:
                result /= num
            return result

    @staticmethod
    def reverse_p_notation(arithmetic_expression: Stack):
        root_node = arithmetic_expression.pop()
        if root_node in ('+', '*', '-', '/'):
            right_node = Rpn.reverse_p_notation(arithmetic_expression)
            left_node = Rpn.reverse_p_notation(arithmetic_expression)
            return Rpn.__operator_applier(root_node, left_node, right_node)
        else:
            return float(root_node)


if __name__ == '__main__':
    statements_list = '70 2 4 1 - * 4 + / 3.5 0 + /'
    statements_stack = Stack()
    for statement in statements_list.split():
        statements_stack.push(statement)

    print(Rpn.reverse_p_notation(statements_stack))
