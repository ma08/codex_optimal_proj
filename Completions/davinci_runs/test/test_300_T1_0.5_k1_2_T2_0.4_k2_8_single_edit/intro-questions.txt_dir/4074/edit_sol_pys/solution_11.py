
def solve(n, k):
    if n < k:
        return 1
    return n // k + n % k
