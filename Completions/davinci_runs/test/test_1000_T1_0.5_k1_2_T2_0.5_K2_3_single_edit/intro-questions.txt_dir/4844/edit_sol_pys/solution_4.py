

def main():
    # Read input
    N = int(input())
    M = []
    for i in range(N):
        M.append([int(x) for x in input().split()])

    # Initialize array
    A = [0 for x in range(N)]

    # Process
    for i in range(N):
        for j in range(N):
            if i != j:
                A[i] = M[i][j] | A[j]

    # Print result
    print(' '.join([str(x) for x in A]))

if __name__ == "__main__":
    main()
