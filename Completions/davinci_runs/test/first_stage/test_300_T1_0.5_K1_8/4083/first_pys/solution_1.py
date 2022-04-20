

n, k = map(int, input().split())
a = list(map(int, input().split()))

def divide_all(a):
    return [int(i/2) for i in a]

def is_all_equal(a):
    return len(set(a)) == 1

def count_operations(a, k):
    if is_all_equal(a):
        return 0
    if len(a) < k:
        return -1
    c = 0
    while not is_all_equal(a):
        a = divide_all(a)
        c += 1
    return c

print(count_operations(a, k))