

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    i = 0
    total = 0
    while i < n:
        if total + a[i] <= k:
            total += a[i]
            i += 1
        else:
            break

    print(i)

if __name__ == "__main__":
    main()
