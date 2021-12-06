if __name__ == '__main__':
    input()
    container = list(map(int, input().split()))

    first_max = max(container)
    index_first_max = container.index(first_max)
    container.remove(first_max)
    sec_max = max(container)

    print(index_first_max + 1, sec_max)
