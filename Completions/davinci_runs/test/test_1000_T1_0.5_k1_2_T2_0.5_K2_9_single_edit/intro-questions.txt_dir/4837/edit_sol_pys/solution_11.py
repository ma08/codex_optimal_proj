

def main():
    rounds = int(input())
    sven = input()
    friends = int(input())
    friend_symbols = []
    for i in range(friends):

        friend_symbols.append(input())
    actual_score = 0
    for round in range(rounds):
        wins = 0
        ties = 0
        for friend_symbol in friend_symbols:
            if sven[round] == friend_symbol[round]:
                ties += 1
            elif sven[round] == "P" and friend_symbol[round] == "R":
                wins += 1
            elif sven[round] == "R" and friend_symbol[round] == "S":
                wins += 1
            elif sven[round] == "S" and friend_symbol[round] == "P":
                wins += 1
        actual_score += wins * 2
        actual_score += ties

    largest_score = 0
    for round in range(rounds):
        sven_wins = 0
        sven_ties = 0
        for friend_symbol in friend_symbols:
            if sven[round] == friend_symbol[round]:
                sven_ties += 1
            elif sven[round] == "P" and friend_symbol[round] == "R":
                sven_wins += 1
            elif sven[round] == "R" and friend_symbol[round] == "S":
                sven_wins += 1
            elif sven[round] == "S" and friend_symbol[round] == "P":
                sven_wins += 1
        largest_score += sven_wins * 2
        largest_score += sven_ties

    print(actual_score)
    print(largest_score)

main()
