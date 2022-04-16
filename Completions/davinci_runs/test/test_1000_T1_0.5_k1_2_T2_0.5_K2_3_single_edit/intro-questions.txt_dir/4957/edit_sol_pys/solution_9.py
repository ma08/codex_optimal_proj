
from collections import deque

def main():
    n,m = [int(x) for x in input().split()]
    grid = [input() for _ in range(n)]
    d=deque()
    for i in range(n): 
        for j in range(m): 
            if grid[i][j]=='.':
                d.append((i,j))
                break 
        if len(d)>0: 
            break 
    while len(d)>0: 
        x,y=d.popleft()
        for i,j in ((x-1,y),(x,y-1),(x,y+1),(x+1,y)): 
            if 0<=i<n and 0<=j<m and grid[i][j]=='.':
                d.append((i,j))
                grid[i][j]='E'
    for i in grid: 
        print(i)
if __name__ == '__main__':
    main()
