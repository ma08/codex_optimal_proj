

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    if n % 2 == 0:
        ans = a[n // 2 - 1]
    else:
        ans = a[n // 2]
    print(ans)


if __name__ == '__main__':
    main()
