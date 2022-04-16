


def find_max_sum(arr):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far


# Driver function to check the above function
arr = [-2, -3, 4, -1, -2, 1, 5, -3]

print(find_max_sum(arr))
