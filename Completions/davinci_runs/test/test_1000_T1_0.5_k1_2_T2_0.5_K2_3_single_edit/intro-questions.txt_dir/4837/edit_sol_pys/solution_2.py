

def main2():
    rounds = int(input())
    sven = input()
    friends = int(input())
    friends_symbols = []
    for i in range(friends):
        friends_symbols.append(input())
    actual_score = 0
    max_score = 0
    for i in range(rounds):
        sven_symbol = sven[i]
        friends_symbols_in_round = list(map(lambda x: x[i], friends_symbols))
        win_count = friends_symbols_in_round.count(beat_symbol(sven_symbol))
        tie_count = friends_symbols_in_round.count(sven_symbol)
        actual_score += win_count * 2 + tie_count
        max_score += win_count * 2 + (friends - win_count - tie_count)
    print(actual_score)
    print(max_score)

def beat_symbol(symbol):
    if symbol == "R":
        return "S"
    elif symbol == "P":
        return "S"
    else:
        return "R"

def main():
    rounds = int(input())
    sven = input()
    friends = int(input())
    friends_symbols = []
    for i in range(friends):
        friends_symbols.append(input())
    actual_score = 0
    max_score = 0
    for i in range(rounds):
        sven_symbol = sven[i]
        friends_symbols_in_round = list(map(lambda x: x[i], friends_symbols))
        win_count = friends_symbols_in_round.count(beat_symbol(sven_symbol))
        tie_count = friends_symbols_in_round.count(sven_symbol)
        actual_score += win_count * 2 + tie_count
        max_score += win_count * 2 + (friends - win_count - tie_count)
    print(actual_score)
    print(max_score)

def beat_symbol(symbol):
    if symbol == "R":
        return "S"
    elif symbol == "P":
        return "R"
    else:
        return "P"

if __name__ == "__main__":
    main()
