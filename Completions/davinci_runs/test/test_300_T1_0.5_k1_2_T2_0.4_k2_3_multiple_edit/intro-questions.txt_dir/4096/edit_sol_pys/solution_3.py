

def main():
    n, m = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    arr.sort()
    i = 0
    days = 0
    while m > 0 and i < n:
        m -= arr[i]
        i += 1
        days += 1
    if m > 0:
        print(-1)
        return
    print(days)


if __name__ == "__main__":
    main()
