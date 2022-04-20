

def solve(n, a):
    if n == 1:
        return 0

    a.sort()
    count = 1
    for i in range(n-1):
        if a[i+1] - a[i] != 1:
            count += 1

    return count


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(n, a))
