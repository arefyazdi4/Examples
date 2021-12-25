from stackClass import Stack


class ReversePolishNotation:
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
        elif operator == '*':
            result = args[0]
            for num in args[1:]:
                result = result / num
            return result

    @staticmethod
    def rpn(arithmetic_expression: Stack):
        first_node = arithmetic_expression.pop()
        if first_node in ('+', '*', '-', '/'):
            second_node = ReversePolishNotation.rpn(arithmetic_expression)
            third_node = ReversePolishNotation.rpn(arithmetic_expression)
            return ReversePolishNotation.operator_applier(first_node, third_node, second_node)
        else:
            return int(first_node)


if __name__ == '__main__':
    statements = '54+53-*'
    expression = Stack()
    for statement in statements:
        expression.push(statement)

    print(ReversePolishNotation.rpn(expression))
