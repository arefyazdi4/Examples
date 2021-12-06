if __name__ == '__main__':
    (a, b) = map(int, input().split())
    sum_ab = 0
    i = 0
    for j in range(b):
        if i % 2 == 0:
            sum_ab += a
        else:
            sum_ab -= a
        i += 1
    for j in range(a):
        if i % 2 == 0:
            sum_ab += b
        else:
            sum_ab -= b
        i += 1
    print(sum_ab)
