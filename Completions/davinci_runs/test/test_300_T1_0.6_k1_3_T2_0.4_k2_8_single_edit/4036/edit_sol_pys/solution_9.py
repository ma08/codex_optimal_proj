

def main():
    n, k = map(int, input().split())
    if n < k or n == 0:
        print("NO")
        return
    if k == 1 or n == 1:
        print("YES")
        print(n)
        return
    # k >= 2
    if n % (k - 1) == 1:
        print("NO")
        return
    print("YES")
    print(str(2 * (n % (k - 1))) + " " + "1 " * (k - 2) + str(n // (k - 1)))

if __name__ == "__main__":
    main()
