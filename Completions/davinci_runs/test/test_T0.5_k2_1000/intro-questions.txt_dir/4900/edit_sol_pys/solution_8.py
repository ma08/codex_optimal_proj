import sys

def main():
    n = int(sys.stdin.readline().strip())
    dists = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dists[i] = list(map(int, sys.stdin.readline().strip().split()))
    
    # pre-process dists
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
    
    # find two nodes that are not adjacent
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if dists[i][j] == dists[i][0] + dists[0][j]:
                print i + 1, j + 1
                return

main()
