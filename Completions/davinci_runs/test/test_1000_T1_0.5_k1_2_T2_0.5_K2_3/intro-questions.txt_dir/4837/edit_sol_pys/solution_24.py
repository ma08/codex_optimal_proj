

def main():
    rounds = int(input())
    sven_symbol = input()
    friends = int(input())
    friend_symbols = []
    for i in range(friends):
        friend_symbols.append(input())
    actual_score = 0
    for round_num in range(rounds):
        wins = 0
        ties = 0
        for friend_symbol in friend_symbols:
            if sven_symbol[round_num] == friend_symbol[round_num]:
                ties += 1
            elif sven_symbol[round_num] == "P" and friend_symbol[round_num] == "R":
                wins += 1
            elif sven_symbol[round_num] == "R" and friend_symbol[round_num] == "S":
                wins += 1
            elif sven_symbol[round_num] == "S" and friend_symbol[round_num] == "P":
                wins += 1
        actual_score += wins * 2 + ties
    largest_score = 0
    for round_num in range(rounds):
        sven_wins = 0
        sven_ties = 0
        for friend_symbol in friend_symbols:
            if sven_symbol[round_num] == friend_symbol[round_num]:
                sven_ties += 1
            elif sven_symbol[round_num] == "P" and friend_symbol[round_num] == "R":
                sven_wins += 1
            elif sven_symbol[round_num] == "R" and friend_symbol[round_num] == "S":
                sven_wins += 1
            elif sven_symbol[round_num] == "S" and friend_symbol[round_num] == "P":
                sven_wins += 1
        largest_score += sven_wins * 2 + sven_ties
    print(actual_score)
    print(largest_score)

main()
