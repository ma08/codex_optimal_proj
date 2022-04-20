

def main():
    N, M = map(int, input().split())
    A = [[0, 0] for i in range(M)]
    for i in range(M):
        a, b = map(int, input().split())
        A[i] = [a, b]
    print(A)

if __name__ == "__main__":
    main()
