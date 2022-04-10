

def max_sum_of_adjacent_difference(n, m):
    """
    Find max sum of absolute difference between adjacent elements of array of length n with sum m.
    """
    if n == 1:
        return 0
    if m > n * (n-1) / 2:
        return n * (n-1)
    else:
        return m * 2

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(max_sum_of_adjacent_difference(n, m))