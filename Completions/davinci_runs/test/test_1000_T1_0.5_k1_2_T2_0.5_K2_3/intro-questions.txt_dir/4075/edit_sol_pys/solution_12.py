import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10 ** 9 + 7

def main():
    n, m = map(int, input().split())
    a = [int(x) for x in readline().split()]
    b = [int(x) for x in readline().split()]

    a = sorted(a)
    b = sorted(b)

    ans = 0
    for i in range(n):
        ans += max(a[i], b[i])

    print(ans)


if __name__ == '__main__':
    main()
