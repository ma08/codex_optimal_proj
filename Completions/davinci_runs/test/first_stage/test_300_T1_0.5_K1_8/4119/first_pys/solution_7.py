

import sys

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()

    ans = 0
    for i in range(m):
        ans += abs(x[i] - x[i-1])

    print(ans)

if __name__ == "__main__":
    main()