

def solve(N):
    if N % 2 == 0:
        return N
    return 2 * N

N = int(input())
print(solve(N))
