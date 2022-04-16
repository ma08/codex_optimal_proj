
def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
    for i in range(n):
        a[i] = a[i] - 1
    for i in range(1, n, 2):
        a[i], a[i - 1] = a[i - 1], a[i]
    for i in range(n - 1, 0, -2):
        a[i], a[i - 1] = a[i - 1], a[i]
    for i in range(n - 1, 0, -1):
        a[i], a[i - 1] = a[i - 1], a[i]
    for i in range(n - 1, 0, -2):
        a[i], a[i - 1] = a[i - 1], a[i]
    for i in range(n):
        print(a[i] + 1)


if __name__ == '__main__':
    main()
