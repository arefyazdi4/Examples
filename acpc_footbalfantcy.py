def gkps(player: list):
    (name,
     position,
     minutes_played,
     number_of_goals,
     number_of_assists,
     number_of_goals_conceded,
     number_of_saves,
     number_of_penalty_saves,
     number_of_penalty_misses,
     number_of_yellow_cards,
     number_of_red_cards,
     number_of_own_goals) = player
    final_score = 0
    if int(minutes_played) >= 60:
        final_score += 2
    else:
        final_score += 1

    final_score += int(number_of_assists) * 3
    final_score += int(number_of_penalty_misses) * (-2)
    final_score += int(number_of_yellow_cards) * (-1)
    final_score += int(number_of_red_cards) * (-3)
    final_score += int(number_of_own_goals) * (-2)

    final_score += int(number_of_goals) * (6)
    if int(number_of_own_goals) == 0: final_score += 4
    final_score += (int(number_of_goals_conceded) // 2) * (-1)
    final_score += (int(number_of_saves) // 3) * (1)
    final_score += int(number_of_penalty_saves) * (5)

    return name, final_score


def defs(player: list):
    (name,
     position,
     minutes_played,
     number_of_goals,
     number_of_assists,
     number_of_goals_conceded,
     number_of_penalty_misses,
     number_of_yellow_cards,
     number_of_red_cards,
     number_of_own_goals) = player

    final_score = 0
    if int(minutes_played) >= 60:
        final_score += 2
    else:
        final_score += 1
    final_score += int(number_of_assists) * 3
    final_score += int(number_of_penalty_misses) * (-2)
    final_score += int(number_of_yellow_cards) * (-1)
    final_score += int(number_of_red_cards) * (-3)
    final_score += int(number_of_own_goals) * (-2)

    final_score += int(number_of_goals) * (6)
    if int(number_of_own_goals) == 0: final_score += 4
    final_score += (int(number_of_goals_conceded) // 2) * (-1)

    return name, final_score


def fwds(player: list):
    (final_score,
     name,
     position,
     minutes_played,
     number_of_goals,
     number_of_assists,
     number_of_penalty_misses,
     number_of_yellow_cards,
     number_of_red_cards,
     number_of_own_goals,) = player
    if position != 'FWD':
        return 'Error For Forward Player'
    if minutes_played < 60:
        final_score += 1
    else:
        final_score += 2
    final_score += number_of_goals * 4
    final_score += number_of_assists * 3
    final_score -= number_of_penalty_misses * 2
    final_score -= number_of_yellow_cards
    final_score -= number_of_red_cards * 3
    final_score -= number_of_own_goals * 2
    return name, final_score


def mids(player):
    final_score = 0
    (name, name_position, minutes_played, number_of_goals, number_of_assists, number_of_goals_conceded,
     number_of_penalty_misses, number_of_yellow_cards, number_of_red_cards, number_of_own_goals) = player

    if int(minutes_played) >= 60:
        final_score += 2
    else:
        final_score += 1
    final_score += int(number_of_goals) * 5
    final_score += int(number_of_assists) * 3
    final_score += int(number_of_penalty_misses) * (-2)
    final_score += int(number_of_yellow_cards) * (-1)
    final_score += int(number_of_red_cards) * (-3)
    final_score += int(number_of_own_goals) * (-2)
    if int(number_of_own_goals) == 0: final_score += 1

    return name, final_score


if __name__ == '__main__':
    players_list = list()
    try:
        while True:
            player_list = input().split()
            players_list.append(player_list)

    except EOFError:
        score = list()
        for player in players_list:
            if player[1] == 'MID':
                score.append(mids(player))
            elif player[1] == 'DEF':
                score.append(defs(player))
            elif player[1] == 'FWD':
                score.append(fwds(player))
            elif player[1] == 'GKP':
                score.append(gkps(player))

        score.sort(key=lambda n: n[1], reverse=True)
        print(score[0][0])
