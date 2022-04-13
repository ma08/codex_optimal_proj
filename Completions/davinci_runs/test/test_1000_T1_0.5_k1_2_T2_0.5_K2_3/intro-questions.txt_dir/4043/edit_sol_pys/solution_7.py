

def main():
    n, d, k = [int(x) for x in input().split()]
    if d == 1:
        if n <= k + 1:
            print("YES")
            print("\n".join(["{} {}".format(1, x) for x in range(2, n + 1)]))
        else:
            print("NO")
    elif d == 2:
        if n <= 2 * k + 1:
            print("YES")
            print("1 2")
            print("\n".join(["{} {}".format(2, x) for x in range(3, n + 1)]))
        else:
            print("NO")
    elif d == 3:
        if n <= 3 * k + 1:
            print("YES")
            print("1 2")
            print("2 3")
            print("\n".join(["{} {}".format(3, x) for x in range(4, n + 1)]))
        else:
            print("NO")
    else:
        if n <= 4 * k + 1:
            print("YES")
            print("1 2")
            print("2 3")
            print("1 4")
            print("\n".join(["{} {}".format(4, x) for x in range(5, n+1)]))
        else:
            print("NO")

if __name__ == '__main__':
    main()
