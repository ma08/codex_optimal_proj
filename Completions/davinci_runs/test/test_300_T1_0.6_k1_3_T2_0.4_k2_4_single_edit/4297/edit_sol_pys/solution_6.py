
def solve(N):
    if N % 2 == 0:
        return N
    else:
        return 2 * N

if __name__ == "__main__":
    N = int(input())
    print(solve(N))
