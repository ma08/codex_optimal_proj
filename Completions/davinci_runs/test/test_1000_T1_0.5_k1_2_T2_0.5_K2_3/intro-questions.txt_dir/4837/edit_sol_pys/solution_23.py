

def main():
    rounds = int(input())
    sven_choices = input()
    friends = int(input())
    friends_symbols = []
    for i in range(friends):
        friends_symbols.append(input())
    actual_score = 0
    max_score = 0
    for i in range(rounds):
        sven_choice = sven_choices[i].upper()
        if sven_choice == "R":
            actual_score += friends_symbols.count("P")
            max_score += friends - friends_symbols.count("S")
        elif sven_choice == "P":
            actual_score += friends_symbols.count("S")
            max_score += friends - friends_symbols.count("R")
        else:
            actual_score += friends_symbols.count("R")
            max_score += friends - friends_symbols.count("P")
    print(actual_score)
    print(max_score)
    if actual_score == max_score:
        print("Tie")
    elif actual_score > max_score:
        print("Sven")
    else:
        print("Emma")

if __name__ == "__main__":
    main()
