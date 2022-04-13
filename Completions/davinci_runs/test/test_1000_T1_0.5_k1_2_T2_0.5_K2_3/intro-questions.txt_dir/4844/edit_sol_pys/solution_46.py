

def main():
    # Read input
    N = int(input())
    M = [[int(x) for x in input().split()] for i in range(N)]

    # Initialize array A
    A = [0] * N

    # Process
    for i in range(N):
        for j in range(N):
            if i != j:
                A[i] = M[i][j] | A[j]

    # Print result
    print(' '.join([str(x) for x in A]))

if __name__ == "__main__":
    main()
