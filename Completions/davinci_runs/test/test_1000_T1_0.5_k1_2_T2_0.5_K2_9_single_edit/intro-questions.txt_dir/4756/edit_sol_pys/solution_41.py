
def main():
    n = int(input())
    xy = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        xy.append((x_i, y_i))
    xy.sort()
    x = [xy[i][0] for i in range(n)]
    y = [xy[i][1] for i in range(n)]
    if n % 2 == 1:
        x_n = x[n // 2]
        y_n = y[n // 2]
    else:
        x_n = (x[n // 2 - 1] + x[n // 2]) / 2.0
        y_n = (y[n // 2 - 1] + y[n // 2]) / 2.0
    print(y_n - x_n)


if __name__ == '__main__':
    main()
