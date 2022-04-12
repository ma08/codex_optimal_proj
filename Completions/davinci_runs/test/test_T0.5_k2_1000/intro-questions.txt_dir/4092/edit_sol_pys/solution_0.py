

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    s = [0] * (n + 1)  # s[i] = a[0] + a[1] + ... + a[i-1]
    for i in range(1, n + 1):  # s[0] = 0
        s[i] = s[i - 1] + a[i - 1]
    d = {}  # d[s[i]] = i
    for i in range(n + 1):  # d[s[i]] = i
        if s[i] in d:  # if s[i] is already in d, add i to d[s[i]]
            d[s[i]].append(i)  # d[s[i]] = [i]
        else:
            d[s[i]] = [i]
    ans = 0
    for i in d:  # for each key in d
        if len(d[i]) > 1:  # if there are more than one i that s[i] = key
            ans += len(d[i]) - 1  # add the number of i that s[i] = key - 1
    print(ans)

if __name__ == '__main__':
    main()
