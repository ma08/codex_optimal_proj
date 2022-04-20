

def max_beauty(n, k, x, a):
    if x < k:
        return -1
    if x == n:
        return sum(a)
    sum_a = 0
    for i in range(k):
        sum_a += a[i]
    max_sum_a = sum_a
    for i in range(k, n):
        sum_a += a[i] - a[i-k]
        max_sum_a = max(max_sum_a, sum_a)
    return max_sum_a


if __name__ == "__main__":
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_beauty(n, k, x, a))