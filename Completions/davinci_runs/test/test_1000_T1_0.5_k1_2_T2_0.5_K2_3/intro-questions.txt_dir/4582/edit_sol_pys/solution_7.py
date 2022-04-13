# https://codeforces.com/problemset/problem/1185/A


def main():
    a, b, c = [int(x) for x in input().split()]
    if c < a:
        print(b + c)
    elif c > b:
        print(b + a + b - c)
    else:
        print(a + b)


if __name__ == '__main__':
    main()
