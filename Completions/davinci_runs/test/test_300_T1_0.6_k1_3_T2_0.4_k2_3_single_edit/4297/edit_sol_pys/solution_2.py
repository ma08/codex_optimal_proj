
def solve(N):
    if N % 2 == 0:
        return N / 2
    else:
        return N

N = int(input())
print(solve(N))
