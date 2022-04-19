
import sys

def main():
    # Read input from stdin and split the lines
    lines = sys.stdin.read().splitlines()
    # Convert the first 3 lines to integers
    a = [list(map(int, lines[i].split())) for i in range(3)]
    # Convert the 4th line to an integer
    n = int(lines[3])
    # Convert the last n lines to integers
    b = [int(lines[i]) for i in range(4, 4+n)]

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
    print('Yes' if bingo else 'No')

if __name__ == '__main__':
    main()
