# https://atcoder.jp/contests/abc079/tasks/abc079_a


def main():
    n = input()
    if n[0] == n[1] and n[1] == n[2]:
        print(0)
        return
    if n[1] == n[2] and n[2] == n[3]:
        return
    if a[-1] - 1 == a[-2]:
        print(a[-1] - a[0])
        return
    print(min(a[-1] - a[1], a[-2] - a[0]))


if __name__ == "__main__":
    main()
