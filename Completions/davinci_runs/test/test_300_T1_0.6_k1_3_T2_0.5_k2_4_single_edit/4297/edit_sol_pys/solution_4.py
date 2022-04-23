

def solve(n):
    return n if n % 2 == 0 else 2 * n

n = int(input())
print(solve(n))
