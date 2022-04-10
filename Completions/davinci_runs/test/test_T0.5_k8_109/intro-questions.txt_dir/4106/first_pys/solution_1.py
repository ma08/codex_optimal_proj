

def find_max_beauty(n, k, x, a):
    # if x < k, then we can't satisfy the condition
    if x < k:
        return -1
    
    # if x >= k, then we can satisfy the condition
    # we can skip the first k-1 elements
    beauty = sum(a[k-1:])
    for i in range(k-1, n):
        if a[i] > a[i-k]:
            beauty += a[i] - a[i-k]
    return beauty

# n, k, x = map(int, input().split())
# a = list(map(int, input().split()))

# print(find_max_beauty(n, k, x, a))

assert find_max_beauty(5, 2, 3, [5, 1, 3, 10, 1]) == 18
assert find_max_beauty(6, 1, 5, [10, 30, 30, 70, 10, 10]) == -1
assert find_max_beauty(4, 3, 1, [1, 100, 1, 1]) == 100