

def main():
    word = input()
    for i in range(5):
        for char in word:
            if i == 0 or i == 4:
                print(".." + ("#" if char in "AEIOUY" else "*") + "..", end=" ")
            elif i == 1 or i == 3:
                print(".#" + ("#" if char in "AEIOUY" else "*") + ".#", end=" ")
            else:
                print("#." + char.upper() + "." + ("#" if char in "AEIOUY" else "*"), end=" ")
        print()

main()
