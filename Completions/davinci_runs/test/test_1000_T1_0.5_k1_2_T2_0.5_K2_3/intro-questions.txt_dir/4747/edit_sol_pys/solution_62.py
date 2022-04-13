
n, k = map(int, input().split())

def solve(n, k, acc = 0):
    if k == 0:
        return acc
    elif k == 1:
        return (n + acc) // 2
    else:
        return solve(n // 2, k - 1, n % 2 + acc)

print(solve(n, k))
