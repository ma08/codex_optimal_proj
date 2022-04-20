

def main():
    N, M = [int(i) for i in input().split()]
    A = []
    for i in range(N):
        A.append([int(i) for i in input().split()])
    A = sorted(A, key=lambda x: (x[0], sum(x)))
    print(max(abs(A[i][0] - A[i+1][0]) for i in range(N-1)))

if __name__ == '__main__':
    main()