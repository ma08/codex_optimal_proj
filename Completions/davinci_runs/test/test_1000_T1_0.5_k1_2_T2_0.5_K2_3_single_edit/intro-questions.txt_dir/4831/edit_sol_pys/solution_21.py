

def main():
    word = input()
    for i in range(6):
        for char in word:
            if i == 0 or i == 5:
                print(".." + ("#" if char in "AEIOUY" else "*") + "..", end="")
            elif i == 1 or i == 4:
                print(".#" + ("#" if char in "AEIOUY" else "*") + ".#", end="")
            else:
                print("#." + char + "." + ("#" if char in "AEIOUY" else "*"), end="")
        print()

main()
