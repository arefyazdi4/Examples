class Error(Exception):
    pass


class TooSmall(Error):
    pass


class TooSBig(Error):
    pass


if __name__ == '__main__':
    try:
        print("try it")

    except NameError as error:
        print(error)

    else:
        print("i gone run if error doesn't happened")

    finally:
        print("i gone rune anyway and any thing no mater if error happened")

    num = 10
    while True:
        try:
            new_num = int(input("say my name?!"))
            if new_num < num:
                raise TooSmall    # or raise ValueError('wrong dude')
            elif new_num > num:
                raise TooSBig
            print("you are god damn Right")
            break

        except TooSmall:
            print("too short")
        except TooSBig:
            print("too large it hurt")



