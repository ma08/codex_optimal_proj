
def solve(n):
    if n % 2 == 0:
        return n
    else:
        return 2 * n


n = int(input())
print(solve(n))
