

def main():
    n, m = map(int, input().split())
    a = [0] * n
    for _ in range(m):
        l, r, x = map(int, input().split())
        for i in range(l-1, r):
            a[i] = x
    print(*a)


if __name__ == '__main__':
    main()
