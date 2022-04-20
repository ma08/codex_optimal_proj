

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b

    for i in range(M):
        for j in range(M):
            if A[i] == B[j]:
                print(A[i])
                exit()
    print(-1)

if __name__ == "__main__":
    main()
