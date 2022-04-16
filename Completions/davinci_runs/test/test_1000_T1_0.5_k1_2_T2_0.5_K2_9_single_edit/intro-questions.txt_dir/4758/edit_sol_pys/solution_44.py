

import sys

def main():
    N,T = map(int,sys.stdin.readline().split())
    M = sys.stdin.readline().split()
    for i in range(len(M)):
        M[i] = int(M[i])
    M.sort()
    ans = 0
    if N <= T:
        ans = M[0]
    else:
        ans = M[N-T]
    print(ans)

if __name__ == "__main__":
    main()
