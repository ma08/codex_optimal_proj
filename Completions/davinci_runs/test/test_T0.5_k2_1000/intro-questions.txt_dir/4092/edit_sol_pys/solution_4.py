
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    for i in range(n):
        a[i] = a[i]
    s = [0] * n
    s[0] = a[0]
    for i in range(1, n):
        s[i] = s[i - 1] + a[i]
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
