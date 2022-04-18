

import sys, math
 
def main():   
    n,m = map(int, sys.stdin.readline().split())
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print(n-1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if [i,j] not in edges and [j,i] not in edges:
                print(i,j)
 
if __name__ == '__main__':
    main()
