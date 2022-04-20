

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    days = 0
    pages = 0
    for i in range(n):
        pages += max(0, a[i] - i)
        if pages >= m:
            print(i + 1)
            return
    print(-1)

main()