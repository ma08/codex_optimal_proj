
# Written by: Eric Wright 
# Date: 1/28/2020

import sys

def main():
    # get input from stdin
    N, M = [int(x) for x in input().split()]
    grid = []
    for i in range(N):
        grid.append(input())
    # get the number of columns that are not blank
    count = 0
    for i in range(M):
        # if the column is not blank, increment count
        if grid[0][i] == '$':
            count += 1
    print(count)

if __name__ == "__main__":
    main()
