

def solve():
    _, k = map(lambda x: int(x), input().split())
    a = list(map(lambda x: int(x), input().split()))[:k]

    min_a = min(a)
    max_a = max(a)
    if max_a - min_a > 1:
        return -1

    cnt = [0] * (max_a + 1)  # 配列の要素数はmax_a + 1
    for elem in a:
        cnt[elem] += 1

    if max_a - min_a == 1:
        if cnt[min_a] < k and cnt[max_a] < k:
            return -1
        else:
            return max(cnt[min_a], cnt[max_a]) - min(cnt[min_a], cnt[max_a])
    else:
        return 0


print(solve())
