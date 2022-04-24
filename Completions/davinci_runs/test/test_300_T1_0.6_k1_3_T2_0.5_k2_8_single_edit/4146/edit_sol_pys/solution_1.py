
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]

    cnt = [0] * (10 ** 5 + 1)
    for i in range(n):
        cnt[a[i]] += 1

    m = 10 ** 5
    for i in range(10 ** 5 + 1):
        if cnt[i] == 0:
            continue
        if cnt[i] == 2:
            m = min(m, 2)
            continue
        if cnt[i] > 2:
            m = min(m, cnt[i] - 1)

    print(m)

if __name__ == '__main__':
    main()
