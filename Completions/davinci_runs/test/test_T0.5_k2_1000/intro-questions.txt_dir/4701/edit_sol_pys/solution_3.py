def solve(n, k):
    if n == 0:
        return 0
    else:
        return min(solve(n-1, k) * 2, solve(n-1, k) + k)

def solve(n, k):
    if n == 0:
        return 0
    else:
        return min(solve(n-1, k) * 2, solve(n-1, k) + k)

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(solve(n, k))
