
# Solution

def main():
    word = input().strip()
    for i in range(0, 5):
        for c in word:  # for each character in the word
            if i == 0:  # first line
                print("..#.." if c in "AEIOU" else "..*..", end="")  # print the first line
            elif i == 1:  # second line
                print(".#.#." if c in "AEIOU" else ".*.*.", end="")  # print the second line
            elif i == 2:  # third line
                print("#." + c + ".#" if c in "AEIOU" else "*." + c + ".*", end="")  # print the third line
            elif i == 3:  # fourth line
                print(".#.#." if c in "AEIOU" else ".*.*.", end="")  # print the fourth line
            elif i == 4:  # fifth line
                print("..#.." if c in "AEIOU" else "..*..", end="")  # print the fifth line
        print()  # print new line


if __name__ == "__main__":
    main()
