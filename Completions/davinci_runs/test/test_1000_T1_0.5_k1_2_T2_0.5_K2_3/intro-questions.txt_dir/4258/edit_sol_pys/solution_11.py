# https://atcoder.jp/contests/abc151/tasks/abc151_c


def main():
    N, M = map(int, input().split())
    AC_count = 0
    penalty_count = 0
    for i in range(M):
        p, s = input().split()
        if s == "AC":
            AC_count += 1
            penalty_count += int(p)
    print(AC_count, penalty_count)


if __name__ == '__main__':
    main()
