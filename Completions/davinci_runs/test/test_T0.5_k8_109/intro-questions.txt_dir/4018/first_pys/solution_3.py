


def main():
    n, k = (int(x) for x in input().split())
    s = input()
    cost = 0
    for i in range(1, n+1):
        cost += i
        if cost >= k:
            print(n-i)
            return
    print(-1)


if __name__ == "__main__":
    main()