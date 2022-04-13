import sys

from sys import stdin

def main():
    N, M = [int(x) for x in stdin.readline().rstrip().split()] 
    grid = [stdin.readline().rstrip() for _ in range(N)]
    for i in range(N - 1, -1, -1): 
        for j in range(M): 
            if grid[i][j] == 'V': 
                if i + 1 < N and grid[i + 1][j] == '.': 
                    grid[i + 1] = grid[i + 1][:j] + 'V' + grid[i + 1][j + 1:] 
                if j - 1 >= 0 and grid[i][j - 1] == '.': 
                    grid[i] = grid[i][:j - 1] + 'V' + grid[i][j:] 
                if j + 1 < M and grid[i][j + 1] == '.': 
                    grid[i] = grid[i][:j + 1] + 'V' + grid[i][j + 2:] 
    for i in range(N): 
        print(grid[i]) 

if __name__ == '__main__': 
    main() 
