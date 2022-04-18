

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
        x_m = x[n // 2]
        y_m = y[n // 2]
    else:
        x_m = (x[n // 2 - 1] + x[n // 2]) / 2
        y_m = (y[n // 2 - 1] + y[n // 2]) / 2
    print(y_m - x_m + 1)

if __name__ == '__main__':
    main()
