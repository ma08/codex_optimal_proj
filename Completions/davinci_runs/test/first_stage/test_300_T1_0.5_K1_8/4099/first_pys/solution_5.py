

import sys

def main():
    n, k, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    avg = (sum(a) + m) / n
    if avg >= m:
        print(m)
    else:
        print(-1)

if __name__ == '__main__':
    main()