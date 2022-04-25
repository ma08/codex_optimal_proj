

def main():
    n, d, k = [int(x) for x in input().split()]
    if d == 1:
        if n <= k * d + 1:
            print("YES")
            print("\n".join(["1 {}".format(x) for x in range(2, n+1)]))
        else:
            print("NO")
    else:
        if n <= k * d + 1:
            print("YES")
            print("\n".join(["{} {}".format(x, x+1) for x in range(2, d-1)]))
            print("{} {}".format(1, d))
            print("\n".join(["{} {}".format(d, x) for x in range(d+1, n+1)]))
        else:
            print("NO")

if __name__ == '__main__':
    main()
