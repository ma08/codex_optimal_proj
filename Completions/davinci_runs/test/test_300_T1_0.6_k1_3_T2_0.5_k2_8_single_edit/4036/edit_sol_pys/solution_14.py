

def main():
    n, k = map(int, input().split())
    if n < k or k < 2:
        print("NO")
        return
    if n == k:
        print("YES")
        print(*[1] * k)
        return
    a = [1] * k
    a[0] = n - k + 1
    print("YES")
    print(*a)

if __name__ == "__main__":
    main()
