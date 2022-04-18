

def main():
    # read input
    N = int(input())
    M = []
    for i in range(N):
        M.append([int(x) for x in input().split()])

    # initialize array
    A = [0] * N

    # process
    for i in range(N):
        for j in range(N):
            if i != j:
                A[i] = M[i][j] | A[j]

    # print result
    print(' '.join([str(x) for x in A]))

if __name__ == "__main__":
    main()
