

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]

    a.sort()

    if n % 2 == 0:
        print(a[n//2 - 1])
    else:
        print(a[n//2])


if __name__ == "__main__":
    main()
