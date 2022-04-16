
 
import sys

def main():
    N, M, L = map(int, sys.stdin.readline().split())
    horror = map(int, sys.stdin.readline().split())
    sim = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split()) - 1
        sim[a].add(b)
        sim[b].add(a)
    HI = [0] * N 
    for i in range(1, N):
        if i in horror: HI[i] = 0
        else: HI[i] = max([HI[j] for j in sim[i]] + [float('inf')]) + 1
    print(HI.index(max(HI)) + 1)
 
if __name__ == '__main__':
    main()
