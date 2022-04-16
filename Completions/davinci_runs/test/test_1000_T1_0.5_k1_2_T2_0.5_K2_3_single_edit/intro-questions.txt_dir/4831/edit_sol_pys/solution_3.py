

    vowels = "AEIOUY"
def main():
    word = input()
    for i in range(5):
        for char in word:
            if i == 0 or i == 4:
                print(".." + ("#" if char in vowels else "*") + "..", end="")
            elif i == 1 or i == 3:
                print(".#" + ("#" if char in vowels else "*") + ".#", end="")
            else:
                print("#." + char + "." + ("#" if char in vowels else "*"), end="")
        print()

main()
