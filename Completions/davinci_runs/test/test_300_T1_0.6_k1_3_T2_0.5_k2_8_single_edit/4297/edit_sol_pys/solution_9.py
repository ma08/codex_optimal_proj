

def solve(N):
    return N if N % 2 == 0 else 2 * N

N = int(input())
print(solve(N))
