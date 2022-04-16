

def main():
    rounds = int(input())
    sven = input().upper()
    friends = int(input())
    friends_symbols = []
    for i in range(friends):
        friends_symbols.append(input().upper())
    actual_score = 0
    max_score = 0
    for i in range(rounds):
        sven_symbol = sven[i].upper()
        friends_symbols_in_round = list(map(lambda x: x[i].upper(), friends_symbols))
        win_count = friends_symbols_in_round.count(beat_symbol(sven_symbol).upper())
        tie_count = friends_symbols_in_round.count(sven_symbol.upper())
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
