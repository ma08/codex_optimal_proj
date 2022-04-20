

def solve(N):
    if N % 2 == 0:
        return N
    else:
        return N * 2

N = int(input())
print(solve(N))
