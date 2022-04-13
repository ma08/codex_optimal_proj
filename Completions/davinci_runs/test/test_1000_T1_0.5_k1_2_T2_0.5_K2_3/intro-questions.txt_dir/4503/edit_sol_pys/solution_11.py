
import sys, math

def main():
    N = int(input())
    A = list(map(int, input().split()))[:N]
    B = list(map(int, input().split()))[:N]
    C = list(map(int, input().split()))[:N-1]
    ans = 0
    for i in range(N):
        ans += B[i]
        if i == 0:
            continue
        if A[i] - A[i-1] == 1:
            ans += C[A[i-1]-1]
    print(ans)

if __name__ == '__main__':
    main()
