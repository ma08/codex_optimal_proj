
import sys
import math

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    print(solve(n, m, p))

def solve(n, m, p):
    left, right = 1, n
    count = 0
    while left <= right:
        c = 0
        for i in range(n):
            if p[i] == mid:
                c += 1
        if c == m:
            count += 1
            for i in range(n):
                if p[i] == mid:
                    for j in range(n):
                        if p[j] == mid:
                            count += (i - j + 1)
                            break
                    break
            break
        elif c > m:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return count

if __name__ == "__main__":
    main()
