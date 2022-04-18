

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    i, j = 0, n-1
    ans = 0
    while i <= j:
        if A[i] > k and A[j] > k: # both sides are larger than k
            break
        elif A[i] <= k and A[j] <= k: # both sides are smaller than k
            ans += 2
            i += 1
            j -= 1
        elif A[i] <= k: # left side is smaller than k
            ans += 1
            i += 1
        else: # right side is smaller than k
            ans += 1
            j -= 1
    print(ans)

if __name__ == '__main__':
    main()
