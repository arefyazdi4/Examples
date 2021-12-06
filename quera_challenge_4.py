
if __name__ == '__main__':
    (n, a, b) = list(map(int, input().split(" ")))
    base = list(map(int, input().split(" ")))
    max_height = base[0]
    a_num = 0
    b_num = 0

    for col_num, column in enumerate(base):
        if column < max_height:
            while column < max_height:
                column += 1
                a_num += 1
        elif column > max_height:
            b_num += 1
            extra_tile = base[col_num] - max_height
            base[col_num] = max_height
            next_col = col_num + 1
            try:
                base[next_col] += extra_tile
            except IndexError:
                if extra_tile == 0 & next_col < n:
                    break
                base.append(0)
                n += 1
                base[next_col] += extra_tile
            while base[next_col] >= max_height:
                col_num = next_col
                extra_tile = base[col_num] - max_height
                base[col_num] = max_height
                next_col = col_num + 1
                try:
                    base[next_col] += extra_tile
                except IndexError:
                    if extra_tile == 0 & next_col < n:
                        break
                    base.append(0)
                    n += 1
                    base[next_col] += extra_tile

    print((a_num*a) + (b_num*b))
