
import sys
import math

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    print(solve(n, m, p))

def solve(n, m, p):
    left, right = 1, n
    mid = (left + right) // 2 # 二分探索
    count = 0
    while left <= right:
        c = 0 # 配列pの中のmidの個数をカウントする
        for i in p:
            if i == mid:
                c += 1
        if c == m:
            count += 1
            for i, j in enumerate(p):
                if j == mid:
                    count += (i - p.index(j) + 1)
            break
        elif c > m:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return count

if __name__ == "__main__":
    main()
