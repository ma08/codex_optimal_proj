
def max_subarray_sum(a):
    max_ending_here = max_so_far = 0
    for x in a:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
print max_subarray_sum(map(int, raw_input().split()))
