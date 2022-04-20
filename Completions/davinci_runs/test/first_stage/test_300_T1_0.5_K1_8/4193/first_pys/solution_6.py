

import sys

def bingo(card, numbers):
    # check rows
    for i in range(3):
        if len(set(card[i]).intersection(numbers)) == 3:
            return True

    # check columns
    for i in range(3):
        if len(set([card[j][i] for j in range(3)]).intersection(numbers)) == 3:
            return True

    # check diagonals
    if len(set([card[i][i] for i in range(3)]).intersection(numbers)) == 3:
        return True
    if len(set([card[i][2-i] for i in range(3)]).intersection(numbers)) == 3:
        return True

    return False

def main():
    card = []
    for i in range(3):
        card.append(list(map(int, sys.stdin.readline().strip().split())))

    num_numbers = int(sys.stdin.readline().strip())
    numbers = []
    for i in range(num_numbers):
        numbers.append(int(sys.stdin.readline().strip()))

    if bingo(card, numbers):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()