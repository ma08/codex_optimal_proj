

import sys

def main():
    # Read input from stdin
    a = [list(map(int, input().split())) for _ in range(3)] # _ is a dummy variable
    n = int(input())
    b = [int(input()) for _ in range(n)]

    # Check if there is a bingo
    bingo = False # boolean
    for i in range(3):
        if bingo:
            break # break out of the loop
        for j in range(3):
            if a[i][j] in b:
                bingo = True # boolean
                break # break out of the loop
    if not bingo:
        for i in range(3):
            if bingo:
                break # break out of the loop
            for j in range(3):
                if a[j][i] in b:
                    bingo = True # boolean
                    break # break out of the loop
    if not bingo:
        for i in range(3):
            if a[i][i] in b:
                bingo = True # boolean
                break # break out of the loop
    if not bingo:
        for i in range(3):
            if a[i][2-i] in b:
                bingo = True # boolean
                break # break out of the loop

    # Print the result
    print('Yes' if bingo else 'No')

if __name__ == '__main__':
    main()
