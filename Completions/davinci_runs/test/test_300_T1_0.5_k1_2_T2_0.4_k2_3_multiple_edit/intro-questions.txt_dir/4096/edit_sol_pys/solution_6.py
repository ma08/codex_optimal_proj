

def main():
    n, m = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()][:n]
    arr.sort()
    i = 0
    days = 0
    while m > 0:
        if arr[i] <= m:
            m -= arr[i]
            days += 1
        i += 1
        days += 1
        if i == n:
            i = 0
    print(days)


if __name__ == "__main__":
    main()
