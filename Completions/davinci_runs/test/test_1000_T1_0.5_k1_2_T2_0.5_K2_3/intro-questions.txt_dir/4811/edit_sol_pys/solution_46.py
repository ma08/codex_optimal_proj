

def main():
    n = int(input())
    a = [0] * (n + 1)
    for _ in range(n):
        x, y = [int(s) for s in input().split()]
        a[x] = y
    for i in range(1, n + 1):
        print(a[i], end=' ')

if __name__ == '__main__':
    main()
