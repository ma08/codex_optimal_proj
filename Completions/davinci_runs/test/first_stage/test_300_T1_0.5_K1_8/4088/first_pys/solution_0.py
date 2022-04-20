

import sys

def solve(s, b):
    m = len(b)
    ans = [None] * m

    def add(i, j):
        b[i] -= abs(i - j)
        b[j] -= abs(i - j)

    for i in range(m):
        for j in range(m):
            if b[i] == 0:
                break
            if b[i] == abs(i - j):
                add(i, j)
                ans[i] = s[j]
                s = s[:j] + s[j + 1:]
                break
    return ''.join(ans)

def main():
    q = int(input())
    for _ in range(q):
        s = input().strip()
        m = int(input())
        b = list(map(int, input().strip().split()))
        print(solve(s, b))

if __name__ == '__main__':
    main()