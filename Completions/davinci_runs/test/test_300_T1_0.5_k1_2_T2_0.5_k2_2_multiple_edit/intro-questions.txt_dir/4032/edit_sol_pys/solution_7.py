

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i, j = 0, N - 1
    ans = 0
    while i <= j:
        if A[i] > K and A[j] > K:
            break
        elif A[i] <= K and A[j] <= K:
            ans += 2
            i += 1
            j -= 1
        elif A[i] <= K:
            ans += 1
            i += 1
        else:
            ans += 1
            j -= 1
    print(ans)


if __name__ == '__main__':
    main()
