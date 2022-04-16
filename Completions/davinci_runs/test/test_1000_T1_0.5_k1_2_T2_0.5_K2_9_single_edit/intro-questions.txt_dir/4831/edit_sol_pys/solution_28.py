
word = input()

for i in range(5):
    for letter in word:
        if i == 0 or i == 4:
            if letter == word[0]:
                print("..#..", end="")
            elif letter in word[2::3]:
                print("..*..", end="")
            else:
                print("..#..", end="")
        elif i == 1 or i == 3:
            if letter == word[0]:
                print(".#.#.", end="")
            elif letter in word[2::3]:
                print(".*.*.", end="")
            else:
                print(".#.#.", end="")
        elif i == 2:
            if letter == word[0]:
                print("#.{}#".format(letter), end="")
            elif letter in word[2::3]:
                print("*.{}.*".format(letter), end="")
            else:
                print("#.{}#".format(letter), end="")
        if letter != word[-1]:
            print("*", end="")
    print()
