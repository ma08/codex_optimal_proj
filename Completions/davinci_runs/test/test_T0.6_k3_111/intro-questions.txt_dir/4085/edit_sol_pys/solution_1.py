

def solve(n, a):
    a.sort()
    mx = a[-1]
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if a[i] + a[j] == mx:
                return mx * mx
    return -1


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(solve(n, a))


if __name__ == "__main__":
    main()
