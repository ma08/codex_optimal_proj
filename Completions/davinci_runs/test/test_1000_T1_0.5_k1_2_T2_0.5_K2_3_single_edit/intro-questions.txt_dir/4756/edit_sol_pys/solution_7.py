

def main():
    n = int(input())
    xy = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        xy.append((x_i, y_i))
    xy.sort(key=lambda x: x[0])
    xy.sort(key=lambda x: x[1])
    if n % 2 == 1:
        x_n = xy[n // 2][0]
        y_n = xy[n // 2][1]
    else:
        x_n = (xy[n // 2 - 1][0] + xy[n // 2][0]) / 2
        y_n = (xy[n // 2 - 1][1] + xy[n // 2][1]) / 2
    print(y_n - x_n)

if __name__ == '__main__':
    main()
