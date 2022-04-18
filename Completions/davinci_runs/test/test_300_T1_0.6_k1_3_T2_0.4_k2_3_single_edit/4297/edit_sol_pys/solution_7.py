

def solve(N):
    if N % 2 == 1:
        return N
    else:
        return 2 * N

N = int(input())
print(solve(N))
