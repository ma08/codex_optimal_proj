
def solve(n, a):
    for i in range(n):
        if a[i] == 0:
            a[i] = 1
        if (i + 1) == n:
            break
        if a[i] == a[i + 1]:
            a[i + 1] = 0
    return sum(a)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))


if __name__ == "__main__":
    main()
