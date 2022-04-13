

def main():
    rounds = int(input())
    sven_symbols = input()
    friends = int(input())
    friends_symbols = [input() for i in range(friends)]
    actual_score = 0
    max_score = 0
    for i in range(rounds):
        sven_symbol = sven_symbols[i]
        friends_symbols_in_round = [x[i] for x in friends_symbols]
        win_count = friends_symbols_in_round.count(beat_symbol(sven_symbol))
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
