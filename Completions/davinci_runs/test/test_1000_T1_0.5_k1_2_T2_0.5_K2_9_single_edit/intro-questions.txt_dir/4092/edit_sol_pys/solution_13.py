

import sys

def main():
    with open('input.txt', 'r') as f:
        n = f.readline()
        n = int(n)
        a = f.readline()
        a = a.split()
        for i in range(n):
            a[i] = int(a[i])
        s = [0] * (n + 1)
        s[0] = 0
        for i in range(1, n + 1):
            s[i] = s[i - 1] + a[i - 1]
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
