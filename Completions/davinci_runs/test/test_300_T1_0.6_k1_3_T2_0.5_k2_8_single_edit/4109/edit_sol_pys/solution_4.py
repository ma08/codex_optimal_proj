
import sys, itertools

def main():
    N, M, X = map(int, sys.stdin.readline().split())
    C = []
    A = []
    for _ in range(N):
        c = list(map(int, sys.stdin.readline().split()))
        C.append(c[0])
        A.append(c[1:])
    
    INF = float("inf")
    ans = INF
    for bit in range(1 << N):
        k = [0] * M
        c = 0
        for i in range(N):
            if bit & (1 << i):
                c += C[i]
                for j in range(M):
                    k[j] += A[i][j]
        if min(k) >= X:
            ans = min(ans, c)
    if ans == INF:
        print(-1) 
    else: 
        print(ans)

if __name__ == "__main__":
    main()
