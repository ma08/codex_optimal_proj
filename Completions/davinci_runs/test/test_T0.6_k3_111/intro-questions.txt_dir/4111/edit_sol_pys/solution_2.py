

def solve(n, a):
    # pre-process and build segment tree
    seg_tree = [0] * (n * 4)
    for i in range(n):
        update(i, a[i], seg_tree, 0, n-1, 1)

    # check if the sum of odd and even days are equal
    ans = 0
    for i in range(n):
        if i == 0:
            if query(0, n-2, 0, n-1, 1, seg_tree) == query(1, n-1, 0, n-1, 1, seg_tree):
                ans += 1
        elif i == n - 1:
            if query(0, n-3, 0, n-1, 1, seg_tree) == query(1, n-2, 0, n-1, 1, seg_tree):
                ans += 1
        else:
            if query(0, i - 1, 0, n-1, 1, seg_tree) == query(i + 1, n-1, 0, n-1, 1, seg_tree):
                ans += 1

    return ans


def update(i, new_val, seg_tree, start, end, node):
    # base case
    if start == end:
        seg_tree[node] = new_val
        return
    # recurse
    mid = (start + end) // 2
    if start <= i <= mid:     # if in left half
        update(i, new_val, seg_tree, start, mid, node * 2)
    else:                     # if in right half
        update(i, new_val, seg_tree, mid + 1, end, node * 2 + 1)

    # update the current sum
    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]


def query(i, j, start, end, node, seg_tree, sum=0):
    # base case
    if start > j or end < i:
        return 0
    if start >= i and end <= j:
        return seg_tree[node]
    # recurse
    mid = (start + end) // 2
    p1 = query(i, j, start, mid, node * 2, seg_tree)
    p2 = query(i, j, mid + 1, end, node * 2 + 1, seg_tree)
    return p1 + p2


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
