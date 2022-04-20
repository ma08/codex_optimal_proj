

import sys

def main():
    N = int(sys.stdin.readline())
    h = list(map(int,sys.stdin.readline().split()))
    ans = 0
    for i in range(N):
        if h[i] == 0:
            continue
        ans += 1
        for j in range(i,N):
            if h[j] == 0:
                break
            h[j] -= 1
    print(ans)

if __name__ == '__main__':
    main()