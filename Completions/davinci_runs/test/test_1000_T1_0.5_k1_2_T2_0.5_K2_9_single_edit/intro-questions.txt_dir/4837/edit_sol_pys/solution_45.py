

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
        win_count = 0
        tie_count = 0
        for x in friends_symbols:
            if x[i] == beat_symbol(sven_symbol):
                win_count += 1
            elif x[i] == sven_symbol:
                tie_count += 1
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
