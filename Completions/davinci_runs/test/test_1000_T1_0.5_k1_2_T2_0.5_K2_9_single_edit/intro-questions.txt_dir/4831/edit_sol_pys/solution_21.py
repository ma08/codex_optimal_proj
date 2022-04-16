
def main():
    word = input()
    for i in range(5):
        for char in word:
            if i in [0, 4]:
                print(".." + ("#" if char in "AEIOUY" else "*") + "..", end="")
            elif i in [1, 3]:
                print(".#" + ("#" if char in "AEIOUY" else "*") + ".#", end="")
            else:
                print("#." + char + "." + ("#" if char in "AEIOUY" else "*"), end="")
        print()


main()
