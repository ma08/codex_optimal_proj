
def main():
    t = int(input())
    for i in range(t):
        n, m = [int(x) for x in input().split()]
        # print("n={} m={}".format(n, m))
        if n == m:
            print(n - 1)
        else:
            print(min(n, m - 1))


if __name__ == "__main__":
    main()
