

import sys

def is_bingo(bingo_card, numbers):
    """
    @type bingo_card: list[list[int]]
    @type numbers: list[int]
    @rtype: bool
    """
    bingo_card = [list(map(lambda x: 0 if x in numbers else x, row)) for row in bingo_card]
    if bingo_card[0][0] == 0 and bingo_card[1][1] == 0 and bingo_card[2][2] == 0:
        return True
    if bingo_card[0][2] == 0 and bingo_card[1][1] == 0 and bingo_card[2][0] == 0:
        return True
    for row in bingo_card:
        if row[0] == 0 and row[1] == 0 and row[2] == 0:
            return True
    for column in zip(*bingo_card):
        if column[0] == 0 and column[1] == 0 and column[2] == 0:
            return True
    return False

def main():
    bingo_card = [list(map(int, l.split())) for l in sys.stdin.readlines()[:3]]
    numbers = list(map(int, sys.stdin.readlines()[4:]))
    if is_bingo(bingo_card, numbers):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()