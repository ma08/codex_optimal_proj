

import sys

def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        if a[i] % 2 == 0:
            a[i] /= 2
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()