def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            c += a[i] * a[j]
    print(c)


if __name__ == "__main__":
    main()
