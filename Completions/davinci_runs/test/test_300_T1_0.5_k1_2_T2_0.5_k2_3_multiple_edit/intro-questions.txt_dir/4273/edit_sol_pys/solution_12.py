

# https://atcoder.jp/contests/abc117/tasks/abc117_d

N, K = map(int, input().split())
A = list(map(int, input().split()))


def f(k):
    return sum([(a // k) * k for a in A])


def main():
    print(f(0))


if __name__ == '__main__':
    main()
