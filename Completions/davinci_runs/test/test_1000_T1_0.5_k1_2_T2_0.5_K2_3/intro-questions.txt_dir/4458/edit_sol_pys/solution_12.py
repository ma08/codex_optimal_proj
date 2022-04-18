
def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_inv = [0] * (n + 1)
    for i in range(n):
        p_inv[p[i]] = i
    seg_tree = [0] * (4 * n)
    ans = 0
    for i in range(n):
        ans += i - get_sum(seg_tree, p_inv[i + 1])
        update(seg_tree, p_inv[i + 1])
    print(ans)

def update(seg_tree, i):
    while i < len(seg_tree):
        seg_tree[i] += 1
        i += i & -i

def get_sum(seg_tree, i, k, l, r):
    if r <= i:
        return seg_tree[k]
    if i <= l:
        return 0
    m = (l + r) // 2
    return get_sum(seg_tree, i, 2 * k + 1, l, m) + get_sum(seg_tree, i, 2 * k + 2, m, r)

if __name__ == '__main__':
    main()
