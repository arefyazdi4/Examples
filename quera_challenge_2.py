

def result(ghorfeh):
    final_place = """########.......########
#{0}.......{1}#
########.......########
#{2}.......{3}#
########.......########
#{4}.......{5}#
########.......########
#{6}.......{7}#
#######################""".format(ghorfeh[0], ghorfeh[1], ghorfeh[2], ghorfeh[3],
                                      ghorfeh[4], ghorfeh[5], ghorfeh[6], ghorfeh[7])
    return final_place


def main():

    shop_num = int(input())

    ghorfeh = []

    for i in range(8):
        if i < shop_num:
            ghorfeh.append("ghorfe{0}".format(i+1))
        else:
            ghorfeh.append(".......")


    final_place = result(ghorfeh=ghorfeh)

    print(final_place)


if __name__ == '__main__':
    main()

