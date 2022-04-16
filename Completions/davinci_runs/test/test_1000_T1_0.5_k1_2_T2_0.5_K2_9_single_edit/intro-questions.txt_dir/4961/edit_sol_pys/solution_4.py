
import sys

def main():
    rows, cols = map(int, sys.stdin.readline().strip().split())
    seats = []
    for i in range(rows):
        seats.append(list(sys.stdin.readline().strip()))
    count = 0
    for r in range(rows):
        for c in range(cols):
            if seats[r][c] == 'o':
                if r-1 >= 0 and seats[r-1][c] == 'o':
                    count += 1
                if r+1 < rows and seats[r+1][c] == 'o':
                    count += 1
                if c-1 >= 0 and seats[r][c-1] == 'o':
                    count += 1
                if c+1 < cols and seats[r][c+1] == 'o':
                    count += 1
                if r-1 >= 0 and c-1 >= 0 and seats[r-1][c-1] == 'o':
                    count += 1
                if r-1 >= 0 and c+1 < cols and seats[r-1][c+1] == 'o':
                    count += 1
                if r+1 < rows and c-1 >= 0 and seats[r+1][c-1] == 'o':
                    count += 1
                if r+1 < rows and c+1 < cols and seats[r+1][c+1] == 'o':
                    count += 1
    print count

main()
