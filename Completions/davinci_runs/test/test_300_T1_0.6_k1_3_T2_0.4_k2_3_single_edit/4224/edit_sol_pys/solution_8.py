
def main():
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    for i in range(N):
        if A[i] >= K:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
