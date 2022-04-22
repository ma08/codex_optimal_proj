
def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    if A[i] + A[j] > A[k]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
