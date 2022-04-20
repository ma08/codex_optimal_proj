

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    color = [0] * n
    for i in range(n):
        color[i] = (a[i] - 1) % k + 1
    print('YES')
    print(*color)


if __name__ == '__main__':
    main()