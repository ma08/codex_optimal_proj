# https://codeforces.com/problemset/problem/1185/A


def main():
    a, b, c = [int(x) for x in input().split()]
    print(a + b + c - max(a, b, c))


if __name__ == "__main__":
    main()
