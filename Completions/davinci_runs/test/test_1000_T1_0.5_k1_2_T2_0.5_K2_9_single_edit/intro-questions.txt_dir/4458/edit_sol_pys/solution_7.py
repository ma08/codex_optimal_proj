

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_inv = [-1] * (n + 1)
    for i in range(n):
        p_inv[p[i]] = i
    seg_tree = [0] * (2 * n)
    ans = 0
    for i in range(n):
        ans += i - get_sum(seg_tree, p_inv[i + 1] + 1, 0, 0, len(seg_tree))
        update(seg_tree, p_inv[i + 1] + 1, 1, 0, len(seg_tree))
    print(ans)

def update(seg_tree, i, x, k, n):  # i: index, x: value, k: index of seg_tree, n: length of segment
    seg_tree[k] += x
    if n == 1:
        return
    l, r = k * 2 + 1, k * 2 + 2
    m = n // 2
    if i < m:
        update(seg_tree, i, x, l, m)
    else:
        update(seg_tree, i - m, x, r, n - m)

def get_sum(seg_tree, i, k, l, r):  # i: index, k: index of seg_tree, l: left, r: right
    if r <= i:
        return seg_tree[k]
    if i <= l:
        return 0
    m = (l + r) // 2
    return get_sum(seg_tree, i, 2 * k + 1, l, m) + get_sum(seg_tree, i, 2 * k + 2, m, r)

if __name__ == '__main__':
    main()
