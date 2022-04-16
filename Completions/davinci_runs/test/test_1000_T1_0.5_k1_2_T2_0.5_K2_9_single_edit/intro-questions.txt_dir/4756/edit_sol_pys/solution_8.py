
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
    x_n = sum(x) / n
    y_n = sum(y) / n
    print(y_n - x_n)

if __name__ == '__main__':
    main()
