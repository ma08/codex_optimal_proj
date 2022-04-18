def solve():
    n = int(input())
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        if a == b:
            print(0)
        else:
            print(1)


if __name__ == "__main__":
    solve()
