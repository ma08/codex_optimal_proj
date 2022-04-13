

import sys


def main():
    # Read input
    bingo_card = [[int(x) for x in sys.stdin.readline().split()] for i in range(3)]
    N = int(sys.stdin.readline())
    b_list = [int(sys.stdin.readline()) for i in range(N)]
    # Check if bingo
    for i in range(3):
        if bingo_card[i][0] in b_list and bingo_card[i][1] in b_list and bingo_card[i][2] in b_list:
            print("Yes")
            return
        if bingo_card[0][i] in b_list and bingo_card[1][i] in b_list and bingo_card[2][i] in b_list:
            print("Yes")
            return
    if bingo_card[0][0] in b_list and bingo_card[1][1] in b_list and bingo_card[2][2] in b_list:
        print("Yes")
        return
    if bingo_card[0][2] in b_list and bingo_card[1][1] in b_list and bingo_card[2][0] in b_list:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
