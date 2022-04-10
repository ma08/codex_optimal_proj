

n = int(input())

def solve(n):
    if n == 1:
        return 0
    elif n % 2 == 1:
        return solve(n-1) + 1
    else:
        return solve(n//2) + 1

print(solve(n))