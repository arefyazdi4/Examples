
def smallest_bigger_str(small_str: str):
    small_str_list = list(small_str)
    enum_small_str_list = list(enumerate(small_str_list))
    for index_s, char_s in enum_small_str_list[::-1]:
        partly_small_str_list = small_str_list[index_s:]
        new_partly_small_str_list = sorted(partly_small_str_list, reverse=True)
        if new_partly_small_str_list > partly_small_str_list:
            small_str_list = small_str_list[:index_s]
            small_str_list.append(new_partly_small_str_list[0])
            small_str_list.extend(sorted(new_partly_small_str_list[1:]))
            return ''.join(small_str_list)
    return 'no answer'


if __name__ == '__main__':

    promotion_serial_list = list()
    promotion_num = int(input())
    for _ in range(promotion_num):
        promotion_serial_list.append(input())

    for promotion in promotion_serial_list:
        print(smallest_bigger_str(promotion))

