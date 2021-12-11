def get_items():
    while True:
        try:
            benefit = list(map(int, input("benefit of items").split()))
            weight = list(map(int, input("weight of items").split()))
            break
        except ValueError as input_error:
            print(input_error)

    return benefit, weight


def setup(benefit, weight, capacity):
    worth = list(enumerate(map(lambda b, w: b / w, benefit, weight)))
    worth.sort(key=lambda worthes: worthes[1], reverse=True)
    total_value = 0

    for index, item_worth in worth:
        if capacity == 0:
            break
        if capacity >= weight[index]:
            capacity -= weight[index]
            total_value += benefit[index]
        elif capacity < weight[index]:
            total_value += capacity * item_worth
            capacity -= capacity
    return total_value


if __name__ == '__main__':
    # (benefits, weights) = get_items()
    # capacities = int(input("capacity of backpack"))
    (benefits, weights) = ([5, 8, 3, 2, 7, 9, 4], [7, 8, 4, 10, 4, 6, 4])
    capacities = 22
    print('maximum value that we can store')
    print(setup(benefits, weights, capacities))
