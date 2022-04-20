

import sys

def main():
    N, X = map(int, sys.stdin.readline().rstrip().split())
    L = list(map(int, sys.stdin.readline().rstrip().split()))
    D = 0
    cnt = 1
    for i in range(N):
        D += L[i]
        if D <= X:
            cnt += 1
        else:
            break
    print(cnt)
    return

if __name__ == "__main__":
    main()
