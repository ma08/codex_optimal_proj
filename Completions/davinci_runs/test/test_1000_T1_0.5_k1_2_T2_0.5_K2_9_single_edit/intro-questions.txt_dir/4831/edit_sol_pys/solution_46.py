
def print_letter(c, i):
    if i == 0:
        print("..#.." if c in "AEIOU" else "..*..", end="")
    elif i == 1:
        print(".#.#." if c in "AEIOU" else ".*.*.", end="")
    elif i == 2:
        print("#." + c + ".#" if c in "AEIOU" else "*." + c + ".*", end="")
    elif i == 3:
        print(".#.#." if c in "AEIOU" else ".*.*.", end="")
    elif i == 4:
        print("..#.." if c in "AEIOU" else "..*..", end="")
# Solution

def main():
    word = input()
    for i in range(0, 5):
        for c in word:print_letter(c, i)
        print()
if __name__ == "__main__":
    main()
