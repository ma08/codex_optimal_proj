
import math

def solve(N):
    count = 0
    for a in range(1, int(math.sqrt(N))+1):
        for b in range(1, N):
            if a*b+b > N:
                break
            if a*b+b == N:
                count += 1

    return count

if __name__ == "__main__":
    N = int(input())
    print(solve(N))
