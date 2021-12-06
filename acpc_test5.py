def dupl(matrial, charindex):
    for index, c in enumerate(matrial):
        if index > charindex:
            if c == matrial[charindex]:
                return False
    return True


teams = []


def permutation(keyWord: list, passWord: list = [], passSize=0):
    if passSize == len(passWord):
        teams.append(sorted(passWord))
    else:
        for index, c in enumerate(keyWord):
            if dupl(keyWord, index):
                new_password = passWord.copy()
                new_password.append(c)
                new_keyword = keyWord.copy()
                new_keyword.remove(c)
                permutation(new_keyword, new_password, passSize)


if __name__ == '__main__':
    per_num = int(input())
    person = list(map(int, input().split()))
    permutation(person, passSize=3)

    for team in teams:
        c = teams.count(team)
        for i in range(c - 1):
            teams.remove(team)

    teams_power_dif = []
    for team in teams:
        new_team = (int(team[2]) - int(team[0]), team)
        teams_power_dif.append(new_team)

    teams_power_dif.sort(key=lambda n: n[0])
    for i in teams_power_dif:
        print(i)

    max_dif = 0
    selected_person = []
    check_rep = True
    for i in range(per_num // 3):
        for team in teams_power_dif:
            check_rep = True
            for people in team[1]:
                if people not in selected_person:
                    pass
                else:
                    check_rep = False
            if check_rep:
                max_dif = team[0]
                selected_person.extend(team[1])
        if (len(selected_person)+1)//3 == per_num//3:
            break
    print(max_dif)
