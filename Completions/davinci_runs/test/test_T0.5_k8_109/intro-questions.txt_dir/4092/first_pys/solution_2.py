
import sys
import math

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i - 1]
    d = {}
    for i in range(n + 1):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    ans = 0
    for i in range(n + 1):
        if s[i] not in d:
            continue
        if len(d[s[i]]) > 1:
            ans += len(d[s[i]]) - 1
        d[s[i]].pop(0)
        if len(d[s[i]]) == 0:
            del d[s[i]]
    print(ans)

if __name__ == '__main__':
    main()