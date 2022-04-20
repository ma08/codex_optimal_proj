
import sys

def main():
    # Read input from stdin
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
    n = int(sys.stdin.readline())
    b = [int(sys.stdin.readline()) for _ in range(n)]

    # Check if there is a bingo
    bingo = False
    for i in range(3):
        if bingo:
            break
        for j in range(3):
            if a[i][j] in b:
                bingo = True
                break
    if not bingo:
        for i in range(3):
            if bingo:
                break
            for j in range(3):
                if a[j][i] in b:
                    bingo = True
                    break
    if not bingo:
        for i in range(3):
            if a[i][i] in b:
                bingo = True
                break
    if not bingo:
        for i in range(3):
            if a[i][2-i] in b:
                bingo = True
                break

    # Print the result
    print('Yes' if bingo else 'No', end='')

if __name__ == '__main__':
    main()
