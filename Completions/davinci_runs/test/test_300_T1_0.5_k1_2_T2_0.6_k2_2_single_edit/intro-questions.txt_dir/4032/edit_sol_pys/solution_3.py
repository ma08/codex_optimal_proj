def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        tmp = 0
        while A[i] % 2 == 0:
            tmp += 1
            A[i] //= 2
        ans += tmp


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    i, j = 0, n-1
    ans = 0
    while i <= j:
        if A[i] > k and A[j] > k:
            break
        elif A[i] <= k and A[j] <= k:
            ans += 2
            i += 1
            j -= 1
        elif A[i] <= k:
            ans += 1
            i += 1
        else:
            ans += 1
            j -= 1
    print(ans)

if __name__ == '__main__':
    main()
