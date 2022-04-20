
def main():
    n, m = map(int, input().split())
    a = [0]*n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        s = 0
        for j in range(m):
            s += a[i][j]
        ans = max(ans, s)


def main():
    n = int(input())
    t = input()
    s = ['']*n
    for i in range(n, 0, -1):
        if n%i == 0:
            for j in range(i):
                s[j::i] = t[j::i][::-1]
            t = ''.join(s)
    print(s)

if __name__ == '__main__':
    main()
