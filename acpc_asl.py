from math import factorial


def r_az_n(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def asl(match_num, goal, total_goal=1, reminded_goal=0, possibility=0):
    if reminded_goal == goal:
        return possibility
    else:
        possibility += r_az_n(match_num, total_goal)
        total_goal += 1


if __name__ == '__main__':
    print(r_az_n(4, 2))
