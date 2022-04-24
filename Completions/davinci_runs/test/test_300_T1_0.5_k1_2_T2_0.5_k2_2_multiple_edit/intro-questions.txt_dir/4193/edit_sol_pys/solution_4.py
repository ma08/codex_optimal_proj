
import sys

def main():
    # read input
    bingo_card = [list(map(int, line.split())) for line in sys.stdin]
    N = int(sys.stdin.readline())
    b_list = [int(sys.stdin.readline()) for i in range(N)]
    # check if bingo or not
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
