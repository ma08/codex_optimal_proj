

def solve(n, a):
    if n == 1:
        return a[0]

    if n == 2:
        return a[0] + a[1]

    if n == 3:
        return a[0] + a[1] + a[2]

    a.sort()
    if n == 4:
        return max(a[0] + a[1] + a[2] + a[3], a[0] + a[3] + a[3])

    return max(a[0] + a[1] + a[2] + a[3], a[0] + a[1] + a[3] + a[4])


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(n, a))
