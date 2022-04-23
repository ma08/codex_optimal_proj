from bisect import bisect_left


def lower_bound(A, key):
    i = bisect_left(A, key)
    if i != len(A) and A[i] == key:
        return i
    return -1


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            a = A[i] + A[j]
            k = lower_bound(A, -a)
            if k > j:
                ans += k - j - 1
    print(ans)
