

def main():
    rounds = int(input())
    sven = input()
    friends = int(input())
    friend_symbols = []
    for i in range(friends):
        friend_symbols.append(input())
    actual_score = 0
    for i in range(rounds):
        wins = 0
        ties = 0
        for friend_symbol in friend_symbols:
            if sven[i] == friend_symbol[i]:
                ties += 1
            elif sven[i] == "P" and friend_symbol[i] == "R":
                wins += 1
            elif sven[i] == "R" and friend_symbol[i] == "S":
                wins += 1
            elif sven[i] == "S" and friend_symbol[i] == "P":
                wins += 1
        actual_score += wins * 2 + ties
    largest_score = 0
    for i in range(rounds):
        sven_wins = 0
        sven_ties = 0
        for friend_symbol in friend_symbols:
            if sven[i] == friend_symbol[i]:
                sven_ties += 1
            elif sven[i] == "P" and friend_symbol[i] == "R":
                sven_wins += 1
            elif sven[i] == "R" and friend_symbol[i] == "S":
                sven_wins += 1
            elif sven[i] == "S" and friend_symbol[i] == "P":
                sven_wins += 1
        largest_score += sven_wins * 2 + sven_ties
    print(actual_score)
    print(largest_score)

main()
