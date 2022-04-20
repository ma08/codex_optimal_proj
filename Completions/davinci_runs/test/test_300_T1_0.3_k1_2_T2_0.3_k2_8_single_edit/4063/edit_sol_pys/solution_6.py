

import sys

def main():
    N = int(input())
    D = list(map(int, input().split()))
    D.sort()
    D.reverse()
    ans = 0
    for i in range(N//2):
        if D[i] == D[i+N//2]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
