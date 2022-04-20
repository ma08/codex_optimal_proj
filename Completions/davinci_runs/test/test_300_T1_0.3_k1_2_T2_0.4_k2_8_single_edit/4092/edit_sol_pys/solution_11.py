import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * n
    s[0] = a[0]
    for i in range(1, n):
        s[i] = s[i - 1] + a[i]
    d = {}
    ans = 0
    for i in range(n):
        if s[i] in d:
            ans = max(ans, i - d[s[i]])
        else:
            d[s[i]] = i
    print(n - ans)

if __name__ == '__main__':
    main()
