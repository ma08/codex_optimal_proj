
def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    x.sort()
    y.sort()
    if n % 2 == 1:
        x_n = x[n // 2]
        y_n = y[n // 2]
    else:
        x_n = (x[n // 2 - 1] + x[n // 2]) / 2.0
        y_n = (y[n // 2 - 1] + y[n // 2]) / 2.0
    print(y_n - x_n)

if __name__ == '__main__':
    main()
