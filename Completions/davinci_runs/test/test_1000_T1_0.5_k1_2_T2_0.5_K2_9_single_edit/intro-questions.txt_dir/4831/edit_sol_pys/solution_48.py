

# SOLUTION
word = input()

for i in range(5):
    for letter in word:
        if i == 0 or i == 4 and letter == word[0]:
            print("..#..", end="")
        elif i == 0 or i == 4 and letter in word[2::3]:
            print("..*..", end="")
        elif i == 0 or i == 4:
            print("..#..", end="")
        elif i == 1 or i == 3 and letter == word[0]:
            print(".#.#.", end="")
        elif i == 1 or i == 3 and letter in word[2::3]:
            print(".*.*.", end="")
        elif i == 1 or i == 3:
            print(".#.#.", end="")
        elif i == 2 and letter == word[0]:
            print("#.{}#".format(letter), end="")
        elif i == 2 and letter in word[2::3]:
            print("*.{}.*".format(letter), end="")
        elif i == 2:
            print("#.{}#".format(letter), end="")
        if letter != word[-1]:
            print("*", end="")
    print()
