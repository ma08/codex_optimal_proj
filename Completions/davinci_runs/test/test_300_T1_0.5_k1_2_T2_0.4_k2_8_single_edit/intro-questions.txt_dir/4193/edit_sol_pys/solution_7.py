
import sys


def main():
    # read input
    bingo_card = [list(map(int, line.split())) for line in sys.stdin]
    N = int(sys.stdin.readline())
    b_list = [int(sys.stdin.readline()) for _ in range(N)]
    # check if bingo
    for i in range(3):
        if any(bingo_card[i][j] in b_list for j in range(3)):
            print("Yes")
            return
        if any(bingo_card[j][i] in b_list for j in range(3)):
            print("Yes")
            return
    if any(bingo_card[i][i] in b_list for i in range(3)):
        print("Yes") 
        return 
    if any(bingo_card[i][2-i] in b_list for i in range(3)):
        print("Yes")
        return
    print("No")

if __name__ == "__main__":
    main()
