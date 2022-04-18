

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        a.sort()
        if n % 2 == 1:
            print(a[n // 2])
        else:
            print((a[n // 2] + a[n // 2 - 1]) // 2)


if __name__ == "__main__":
    main()
