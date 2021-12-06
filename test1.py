def func1(b):
    b.append(4)


if __name__ == '__main__':
    a = [1, 2, 3]
    print(a)
    func1(a)
    print(a)
