

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    i = 0
    total = 0
    while i < n:
        if total + a[i] <= m:
            total += a[i]
            i += 1
        else:
            break

    print(i)

if __name__ == "__main__":
    main()
