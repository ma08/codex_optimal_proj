# https://atcoder.jp/contests/abc150/tasks/abc150_c


def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    l = [i for i in range(1, n + 1)]
    x = y = 0
    for i in range(n):
        if p[i] != l[i]:
            x += 1
        if q[i] != l[i]:
            y += 1
    print(abs(x - y))


if __name__ == "__main__":
    main()
