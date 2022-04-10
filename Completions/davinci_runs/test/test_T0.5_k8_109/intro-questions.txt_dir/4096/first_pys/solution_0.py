

def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    if a[0] >= m:
        print(1)
        return

    if sum(a) < m:
        print(-1)
        return

    day = 1
    pages = 0
    for i in range(n):
        pages += max(a[i] - i, 0)
        if pages >= m:
            print(day)
            return
        day += 1

if __name__ == "__main__":
    main()