def get_sound():
    while True:
        try:
            (h1_left, h1_right) = input().split(" ")
            (h2_left, h2_right) = input().split(" ")
            break
        except ValueError as input_error:
            print(input_error)

    left_sound = (h1_left, h2_left)
    right_sound = (h1_right, h2_right)
    final_track = (left_sound, right_sound)
    return final_track


def main():

    final_track = get_sound()

    left_sound = final_track[0]
    right_sound = final_track[1]
    for sound in left_sound:
        if sound in right_sound:
            return "YES"
    return "NO"


if __name__ == '__main__':
    result = main()
    print(result)

