def find_max_subarray(subarray, low_index: int = 0, high_index: int = 0):
    if low_index == high_index:
        return low_index, high_index, subarray[low_index]
    else:
        mid_index = ((low_index + high_index) // 2)
        subareas = [find_max_subarray(subarray, low_index, mid_index),  # left maximum subarray
                    find_max_subarray(subarray, mid_index + 1, high_index),  # right maximum subarray
                    find_max_crossing_subarray(subarray, low_index, mid_index, high_index),  # cross maximum subarray
                    ]
        # return max(subareas, key=lambda data: data[2])
        subareas.sort(key=lambda data: data[2], reverse=True)
        return subareas[0]


def find_max_crossing_subarray(subarray, low_index: int, mid_index: int, high_index: int):
    sum_subarray = 0
    max_low_index = mid_index
    max_sum_subarray_left = subarray[mid_index]
    for i in range(mid_index, low_index - 1, -1):
        sum_subarray += subarray[i]
        if sum_subarray > max_sum_subarray_left:
            max_sum_subarray_left = sum_subarray
            max_low_index = i
    sum_subarray = 0
    max_high_index = mid_index + 1
    max_sum_subarray_right = subarray[mid_index + 1]
    for i in range(mid_index + 1, high_index + 1):
        sum_subarray += subarray[i]
        if sum_subarray > max_sum_subarray_right:
            max_sum_subarray_right = sum_subarray
            max_high_index = i
    return max_low_index, max_high_index, max_sum_subarray_right + max_sum_subarray_left


if __name__ == '__main__':
    listA = [12, -5, -23, 18, -1, -14, -22, 20, 18, -6, 11]
    print(len(listA))
    print(find_max_subarray(listA, 0, len(listA)-1))
