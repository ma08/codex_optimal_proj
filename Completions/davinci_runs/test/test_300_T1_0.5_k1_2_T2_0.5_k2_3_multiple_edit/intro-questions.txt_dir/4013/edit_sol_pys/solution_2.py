# https://codeforces.com/problemset/problem/1208/B


def main():
    a, b, c = map(int, input().split())
    print(max(a, b, c) - min(a, b, c))


if __name__ == "__main__":
    main()
