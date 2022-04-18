

def process(M):
    N = len(M)
    A = [0] * N
    for i in range(N):
        for j in range(N):
            if i != j:
                A[i] = M[i][j] | A[j]
    return A

def main():
    # Read input
    N = int(input())
    M = []
    for i in range(N):
        M.append([int(x) for x in input().split()])

    # Process & Print
    print(' '.join([str(x) for x in process(M)]))

    # Print result
    print(' '.join([str(x) for x in A]))

if __name__ == "__main__":
    main()
