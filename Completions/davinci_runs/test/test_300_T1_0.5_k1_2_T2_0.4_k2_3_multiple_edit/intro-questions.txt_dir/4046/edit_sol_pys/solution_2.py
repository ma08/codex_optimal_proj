
def solve(n, a):
    p = [1]
    for i in range(n - 1):
        if p[-1] + a[i] > 0 and p[-1] + a[i] <= n:
            p.append(p[-1] + a[i])
        else:
            return -1
    return p


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(*solve(n, a))


if __name__ == "__main__":
    main()
