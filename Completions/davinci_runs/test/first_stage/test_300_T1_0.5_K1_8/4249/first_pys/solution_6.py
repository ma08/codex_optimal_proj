

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    days = 0
    for i in range(n):
        if a[i] < i + 1:
            break
        days += 1
        m -= a[i] - i
        if m <= 0:
            break
    if m > 0:
        print(-1)
    else:
        print(days)

if __name__ == "__main__":
    main()