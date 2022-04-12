

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        for i in range(n // 2):
            a[i], a[n - 1 - i] = a[n - 1 - i], a[i]
    else:
        for i in range(n // 2):
            a[i], a[n - 1 - i] = a[n - 1 - i], a[i]

    print(*a)

if __name__ == "__main__":
    main()
