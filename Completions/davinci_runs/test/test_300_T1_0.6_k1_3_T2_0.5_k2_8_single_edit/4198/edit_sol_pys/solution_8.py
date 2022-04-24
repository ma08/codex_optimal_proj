

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if A[i] + B[j] + C[k] >= K:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
