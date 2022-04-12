# https://atcoder.jp/contests/abc086/tasks/arc089_a


def main():
    n = int(input())
    t = 0
    x = 0
    y = 0
    for _ in range(n):
        t_i, x_i, y_i = map(int, input().split())
        dt = t_i - t
        dx = abs(x_i - x)
        dy = abs(y_i - y)
        if dx + dy > dt:
            print("No")
            exit()
        if (dx + dy) % 2 != dt % 2:
            print("No")
            exit()
        t = t_i
        x = x_i
        y = y_i
    print("Yes")


if __name__ == "__main__":
    main()
