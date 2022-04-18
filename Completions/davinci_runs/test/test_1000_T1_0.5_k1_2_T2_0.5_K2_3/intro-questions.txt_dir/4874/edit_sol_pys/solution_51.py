

# Written by: Eric Wright, Zachery Miller
# Date: 1/28/2020

import sys

def main():
    # get input from stdin
    N, M = [int(x) for x in input().split()]
    grid = []
    for i in range(N):
        grid.append(input())
    # get the number of columns that are not blank
    not_blank = 0
    for i in range(M):
        # if the column is not blank, increment count
        if grid[0][i] == '$':
            not_blank += 1
    print(not_blank)

if __name__ == "__main__":
    main()
