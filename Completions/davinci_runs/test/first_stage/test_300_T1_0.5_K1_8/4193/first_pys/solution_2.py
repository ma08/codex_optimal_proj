

import sys

def main():
    a = []
    for _ in range(3):
        a.append([int(x) for x in sys.stdin.readline().split()])
    n = int(sys.stdin.readline())
    b = [int(sys.stdin.readline()) for _ in range(n)]
    bingo = [[False] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                bingo[i][j] = True
    if bingo[0][0] and bingo[0][1] and bingo[0][2]:
        print("Yes")
        return
    if bingo[1][0] and bingo[1][1] and bingo[1][2]:
        print("Yes")
        return
    if bingo[2][0] and bingo[2][1] and bingo[2][2]:
        print("Yes")
        return
    if bingo[0][0] and bingo[1][0] and bingo[2][0]:
        print("Yes")
        return
    if bingo[0][1] and bingo[1][1] and bingo[2][1]:
        print("Yes")
        return
    if bingo[0][2] and bingo[1][2] and bingo[2][2]:
        print("Yes")
        return
    if bingo[0][0] and bingo[1][1] and bingo[2][2]:
        print("Yes")
        return
    if bingo[0][2] and bingo[1][1] and bingo[2][0]:
        print("Yes")
        return
    print("No")

if __name__ == '__main__':
    main()