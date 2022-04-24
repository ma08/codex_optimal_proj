

def main():
    n, k = [int(x) for x in input().split()]
    if n < k:
        print("NO")
        return
    if k == 1:
        if n == 1:
            print("YES\n1")
        else:
            print("NO")
        return
    # k >= 2
    if n % (k - 1) == 0:
        print("YES")
        print(" ".join(["1"] * (k - 1) + [str(n // (k - 1))]))
    else:
        if n % (k - 1) == 1:
            print("NO")
        else:
            print("YES")
            print(" ".join([str(2 * (n % (k - 1)))] + ["1"] * (k - 2) + [str(n // (k - 1))]))

if __name__ == "__main__":
    main()
