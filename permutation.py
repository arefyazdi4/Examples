def dupl(matrial, charindex):
    for index, c in enumerate(matrial):
        if index > charindex:
            if c == matrial[charindex]:
                return False
    return True


def permutation(keyWord, passWord="", passSize=0):
    if passSize == len(passWord):
        print(passWord)

    else:
        keyChar = list(keyWord)
        # print(keyWord , "test1")
        # print(keyChar , "test2")

        for index, c in enumerate(keyChar):
            if dupl(keyChar, index):
                new_password = passWord + c
                # print(passWord ,"test3")
                # print(new_passWord , "test4")
                new_keyword = [
                    keyWord[i]
                    for i in list(
                        filter(
                            lambda n: n != index,
                            [indexs for indexs, s in enumerate(keyChar)],
                        )
                    )
                ]
                # print(new_keyword , "test5")
                # print("".join(new_keyword) ,"test6")

                permutation("".join(new_keyword), new_password, passSize)


def main():
    s = "123759"
    permutation(keyWord=s, passSize=3)


if __name__ == "__main__":
    main()