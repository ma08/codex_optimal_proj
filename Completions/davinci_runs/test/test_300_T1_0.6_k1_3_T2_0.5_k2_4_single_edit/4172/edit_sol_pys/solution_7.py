def solve():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))


    min_a, max_a = min(a), max(a)
    if max_a - min_a > k:
        return -1

    cnt = [0] * (k + 1)
    for elem in a:
        cnt[elem] += 1

    if max_a - min_a == k:
        return cnt[min_a]
    else:
        return 0


print(solve())
