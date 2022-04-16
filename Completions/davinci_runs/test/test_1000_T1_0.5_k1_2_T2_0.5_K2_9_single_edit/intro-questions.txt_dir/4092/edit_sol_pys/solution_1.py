
import bisect
import sys

def main():
    n = sys.stdin.readline()
    n = int(n)
    a = sys.stdin.readline()
    a = a.split()
    for i in range(n):
        a[i] = int(a[i])
    s = [0]
    for i in a:
        s.append(s[-1] + i)
    s.sort()
    ans = 0
    for i in d:
        if len(d[i]) > 1:
            ans += len(d[i]) - 1
    print(ans)

if __name__ == '__main__':
    main()
