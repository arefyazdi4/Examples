
if __name__ == '__main__':
    # default values
    wallet = 0
    min_wal = 0
    max_wal = 0  # max value that we could have at the beginning
    lie_detector = False
    # default index
    state = 0
    money = 1
    time = 2
    result = 3

    # getting and sorting input data (actions)
    num = int(input())
    actions_list = []
    for i in range(num):
        action = input().split(" ")
        actions_list.append(action)
    actions_list.sort(key=lambda n: n[time])

    # Algorithm
    for action in actions_list:
        if action[state] == 'DEP':
            wallet += int(action[money])
            max_wal += int(action[money])
        else:  # action[state] == 'WIT'
            if action[result] == 'OK':
                wallet -= int(action[money])
            else:  # action[result] =  'FAIL'
                if wallet > int(action[money]):
                    lie_detector = True
                max_wal = wallet - int(action[money])
        min_wal = min(wallet, min_wal)
        if min_wal < max_wal & max_wal <= 0:
            lie_detector = True

    if lie_detector:
        print('DOROGHE')
    else:
        print(-min_wal)
