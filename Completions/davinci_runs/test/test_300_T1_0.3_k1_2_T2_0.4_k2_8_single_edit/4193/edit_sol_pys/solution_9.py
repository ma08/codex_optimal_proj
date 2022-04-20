

import sys

def main():
    # Read input from stdin
    a = [list(map(int, input().split())) for _ in range(3)] # a[i][j]
    n = int(input())
    b = [int(input()) for _ in range(n)]

    # Check if there is a bingo
    bingo = False
    for i in range(3): # row
        if bingo:
            break
        for j in range(3): # column
            if a[i][j] in b:
                bingo = True
                break
    if not bingo:
        for i in range(3): # column
            if bingo:
                break
            for j in range(3): # row
                if a[j][i] in b:
                    bingo = True
                    break
    if not bingo:
        for i in range(3): # diagonal
            if a[i][i] in b:
                bingo = True
                break
    if not bingo:
        for i in range(3): # diagonal
            if a[i][2-i] in b:
                bingo = True
                break

    # Print the result
    print('Yes' if bingo else 'No')

if __name__ == '__main__':
    main()
