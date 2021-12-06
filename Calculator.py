import math


class Calculator:
    @staticmethod
    def sum(*args):
        result = 0
        for x in args:
            result = result + x
        return result

    @staticmethod
    def power(num, x=1):
        return num**x

    @staticmethod
    def fac(num):
        num = abs(num)
        result = 1
        if (num == 0) :
            return result
        else:
            while (num > 1):
                result = result * num
                num -= 1
            return result        


if __name__ == '__main__':

    print("===============SUM===================")
    print(Calculator.sum(2 , 3 , 4 , -1))
    print("===============FAC====================")
    print(Calculator.fac(3))
    print(Calculator.fac(0))
    print("===============Power====================")
    print(Calculator.power(2 , 3))
    print(Calculator.power(2 , -1))
    print(Calculator.power(4 , 1/2))
    print(sum(x for x in range(10)))
    it1 = iter([1,2,3,4])
    print(it1.__next__())

