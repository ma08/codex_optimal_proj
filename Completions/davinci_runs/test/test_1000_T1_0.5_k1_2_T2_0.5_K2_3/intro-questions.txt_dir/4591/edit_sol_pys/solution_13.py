
import sys

def main():
    # Read input.
    N, A, B = [int(x) for x in sys.stdin.readline().split()]
    X = [int(x) for x in sys.stdin.readline().split()]

    # Calculate minimum cost.
    cost = A * N
    for i in range(N):
        if i < N - 1:
            if X[i + 1] - X[i] < B:
                cost += A
            else:
                cost += B

    print(cost) 

if __name__ == "__main__":
    main()
