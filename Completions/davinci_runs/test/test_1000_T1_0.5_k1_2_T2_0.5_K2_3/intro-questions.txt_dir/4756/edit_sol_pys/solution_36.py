

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x[i] = x_i
        y[i] = y_i
    x.sort()
    y.sort()
    if n % 2 == 1:
        x_m = x[n // 2]
        y_m = y[n // 2]
    else:
        x_m = (x[n // 2 - 1] + x[n // 2]) / 2
        y_m = (y[n // 2 - 1] + y[n // 2]) / 2
    print(y_m - x_m)

if __name__ == '__main__':
    main()
