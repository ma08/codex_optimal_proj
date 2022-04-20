

def solve(N, M, A):
    return 0

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append([a, b])
    print(solve(N, M, A))

if __name__ == "__main__":
    main()
