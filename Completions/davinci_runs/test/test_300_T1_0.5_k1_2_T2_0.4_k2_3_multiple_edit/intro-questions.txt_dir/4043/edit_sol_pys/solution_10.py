

def main():
    n, d, k = [int(x) for x in input().split()]
    if n <= (d + 1) * k + 1:
        print("YES")
        for i in range(1, d + 1):
            print("{} {}".format(i, i + 1))
        print("\n".join(["{} {}".format(i, i + d + 1) for i in range(d + 2, n + 1)]), end="")
    else:
        print("NO")

if __name__ == '__main__':
    main()
