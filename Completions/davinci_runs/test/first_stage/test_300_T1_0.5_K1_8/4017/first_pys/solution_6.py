

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n
    s = sum(a)
    if s % 2 == 1:
        print(0)
        return
    s //= 2
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + a[i - 1]
    c = [0] * (n + 1)
    for i in range(n, 0, -1):
        c[i] = c[i + 1] + a[i - 1]
    ans = []
    for i in range(1, n + 1):
        if b[i] == s or c[i] == s:
            ans.append(i)
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    main()