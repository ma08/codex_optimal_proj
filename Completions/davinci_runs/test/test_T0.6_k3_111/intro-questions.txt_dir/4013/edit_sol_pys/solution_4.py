

def main():
    # Read input
    n = int(input())
    a = [int(x) for x in input().split()]

    # Find the minimum and maximum value in the array, and the indices of the minimum and maximum values
    min_val = min(a)
    max_val = max(a)
    min_idx = a.index(min_val)
    max_idx = a.index(max_val)

    # If the minimum and maximum values are at different indices, then we can remove either
    # the minimum value or the maximum value and get instability of zero
    if min_idx != max_idx:
        print(0)
    else:
        # Otherwise, we need to find the second smallest and second largest value in the array
        a.remove(min_val)
        a.remove(max_val)
        min_val2 = min(a)
        max_val2 = max(a)

        # The minimum possible instability is the difference between the second largest and
        # second smallest value
        print(max_val2 - min_val2)

if __name__ == "__main__":
    main()
