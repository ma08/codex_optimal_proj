

def main():
    rounds = int(input())
    sven_symbols = list(input())
    friends = int(input())
    friends_symbols = []
    for i in range(friends):
        friends_symbols.append(list(input()))
    actual_score = 0
    max_score = 0
    for i in range(rounds):
        sven_symbol = sven_symbols[i]
        friends_symbols_in_round = list(map(lambda x: x[i], friends_symbols))
        win_count = friends_symbols_in_round.count(beat_symbol(sven_symbol))
        print(win_count, tie_count)
        tie_count = friends_symbols_in_round.count(sven_symbol)
        actual_score += win_count * 2 + tie_count
        max_score += win_count * 2 + (friends - win_count - tie_count)
    print(actual_score)
    print(max_score)

def beat_symbol(symbol):
    if symbol == "R":
        return "P"
    elif symbol == "P":
        return "S"
    else:
        return "R"

if __name__ == "__main__":
    main()
