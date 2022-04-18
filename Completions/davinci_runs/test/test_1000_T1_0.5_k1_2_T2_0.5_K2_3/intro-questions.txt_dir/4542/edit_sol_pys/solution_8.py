

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    points = 0
    for i in range(N):
        points += B[A[i]]
        if (i+1) < N and A[i+1] == A[i] + 1:
            points += C[A[i]]
    print(points)

if __name__ == '__main__':
    main()
