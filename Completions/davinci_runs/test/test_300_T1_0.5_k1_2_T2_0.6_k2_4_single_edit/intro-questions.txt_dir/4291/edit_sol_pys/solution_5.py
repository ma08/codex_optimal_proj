

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    Q = [list(map(int, input().split())) for _ in range(M)]
    print(N, M)
    print(A)
    print(Q)

if __name__ == '__main__':
    main()
