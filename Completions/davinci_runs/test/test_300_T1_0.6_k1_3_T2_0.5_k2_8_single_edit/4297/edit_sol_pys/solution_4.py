

def solve(N):
    if N % 2 == 0:
        return N + 1
    else:
        return 2 * (N + 1)

N = int(input())
print(solve(N))
