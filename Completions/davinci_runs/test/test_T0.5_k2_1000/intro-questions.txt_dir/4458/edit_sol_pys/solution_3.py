

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_inv = [0] * (n)
    for i in range(n):
        p_inv[p[i]] = i
    seg_tree = [0] * (4 * n)
    ans = 0
    for i in range(n):
        ans += i - get_sum(seg_tree, p_inv[i], 0, 0, n)
        update(seg_tree, p_inv[i], 1, 0, n)
    print(ans)

def update(seg_tree, i, x, k, n):
    seg_tree[k] += x
    if n == 1:
        return
    l, r = k * 2 + 1, k * 2 + 2
    m = n // 2
    if i < m:
        update(seg_tree, i, x, l, m)
    else:
        update(seg_tree, i - m, x, r, n - m)

def get_sum(seg_tree, i, k, l, r):
    if r <= i:
        return seg_tree[k]
    if i <= l:
        return 0
    m = (l + r) // 2
    return get_sum(seg_tree, i, 2 * k + 1, l, m) + get_sum(seg_tree, i, 2 * k + 2, m, r)

if __name__ == '__main__':
    main()
