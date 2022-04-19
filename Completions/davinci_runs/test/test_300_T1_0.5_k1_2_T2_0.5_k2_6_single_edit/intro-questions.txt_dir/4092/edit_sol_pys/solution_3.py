

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    d = {}
    for i in range(n + 1):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    ans = 0
    for i in d:
        if len(d[i]) > 1:
            ans += len(d[i]) - 1
    print(ans)

if __name__ == '__main__':
    main()
