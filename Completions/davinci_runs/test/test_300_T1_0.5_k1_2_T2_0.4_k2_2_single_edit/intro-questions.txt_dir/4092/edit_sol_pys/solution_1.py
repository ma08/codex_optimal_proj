

import sys

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] >= a[k - 1] and a[i] > 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
