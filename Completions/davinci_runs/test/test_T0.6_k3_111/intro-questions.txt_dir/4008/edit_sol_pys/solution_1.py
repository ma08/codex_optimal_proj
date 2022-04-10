

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n == k:
        print("YES")
        print(" ".join(str(i % k + 1) for i in a))
        return
    if k * (k + 1) // 2 < n:
        print("NO")
        return
    if n < k:
        print("NO")
        return
    print("YES")
    print(" ".join(str(k - (i % k) + 1) for i in a))


if __name__ == "__main__":
    main()
