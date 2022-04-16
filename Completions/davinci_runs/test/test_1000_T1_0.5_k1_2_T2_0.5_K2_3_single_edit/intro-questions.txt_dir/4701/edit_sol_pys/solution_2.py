

def solve(n, k):
    if n == 1:
        return 0
    else:
        return min(solve(n-1, k) * 2 + 1, solve(n-1, k) + k)

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(solve(n, k))
