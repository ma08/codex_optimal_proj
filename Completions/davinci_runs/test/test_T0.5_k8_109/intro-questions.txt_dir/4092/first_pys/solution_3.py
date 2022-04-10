

def solve(arr):
    """
    >>> solve([1, -5, 3, 2])
    1
    >>> solve([4, -2, 3, -9, 2])
    0
    >>> solve([-1, 1, -1, 1, -1, 1, 1, -1, -1])
    6
    >>> solve([16, -5, -11, -15, 10, 5, 4, -4])
    3
    """
    n = len(arr)
    sums = [0] * (n+1)
    for i in range(1, n+1):
        sums[i] = sums[i-1] + arr[i-1]
    d = {}
    for i in range(n+1):
        if sums[i] in d:
            d[sums[i]] += 1
        else:
            d[sums[i]] = 1
    ans = 0
    for key, value in d.items():
        if value == 1:
            continue
        if value % 2 == 0:
            ans += value // 2
        else:
            ans += value // 2 + 1
    return ans

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))