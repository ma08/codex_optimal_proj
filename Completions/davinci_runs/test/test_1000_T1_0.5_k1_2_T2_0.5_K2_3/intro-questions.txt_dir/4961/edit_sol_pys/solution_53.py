import sys

def main():
    row, col = map(int, sys.stdin.readline().strip().split())
    seats = []
    for i in range(row):
        seats.append(list(sys.stdin.readline().strip()))
    count = 0
    for r in range(row):
        for c in range(col):
            if seats[r][c] == 'o':
                if r-1 >= 0 and seats[r-1][c] == 'o':
                    count += 1
                if r+1 < row and seats[r+1][c] == 'o':
                    count += 1
                if c-1 >= 0 and seats[r][c-1] == 'o':
                    count += 1
                if c+1 < col and seats[r][c+1] == 'o':
                    count += 1
                if r-1 >= 0 and c-1 >= 0 and seats[r-1][c-1] == 'o':
                    count += 1
                if r-1 >= 0 and c+1 < col and seats[r-1][c+1] == 'o':
                    count += 1
                if r+1 < row and c-1 >= 0 and seats[r+1][c-1] == 'o':
                    count += 1
                if r+1 < row and c+1 < col and seats[r+1][c+1] == 'o':
                    count += 1
    print count

main()
