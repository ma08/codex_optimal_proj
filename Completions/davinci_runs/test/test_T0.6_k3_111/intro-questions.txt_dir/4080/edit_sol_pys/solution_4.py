

import sys

def get_min_max(l, r):
    """
    returns the smallest and largest value of the array between l and r, inclusive.
    """
    min_val = min(arr[l:r])
    max_val = max(arr[l:r])
    return (min_val, max_val)

def get_max_diff(segment):
    """
    returns the difference between the largest and smallest values within a segment.
    """
    min_val, max_val = get_min_max(segment[0]-1, segment[1])
    return max_val - min_val

def get_segments_to_use(segments):
    """
    returns the indices of the segments that should be used to get the largest
    difference between the largest and smallest values in the array.
    """
    segments_to_use = []
    for segment in segments:
        l, r = segment
        min_val, max_val = get_min_max(l-1, r)
        max_diff = max_val - min_val
        if max_diff > largest_diff:
            largest_diff = max_diff
            segments_to_use = [segment]
        elif max_diff == largest_diff:
            segments_to_use.append(segment)
    return segments_to_use

def main():
    global arr, largest_diff
    n, m = [int(x) for x in sys.stdin.readline().split()]
    arr = [int(x) for x in sys.stdin.readline().split()]
    # initialize the largest difference to the difference between the max and min
    # of the entire array.
    largest_diff = max(arr) - min(arr)
    segments = []
    for i in range(m):
        segments.append([int(x) for x in sys.stdin.readline().split()])
    # sort the segments by the largest difference between the smallest and largest
    # values in the segment
    segments.sort(key=get_max_diff, reverse=True)
    # get the indices of the segments to use
    segments_to_use = get_segments_to_use(segments)
    # print the largest difference
    print(largest_diff)
    # print the number of segments to use
    print(len(segments_to_use))
    # print the indices of the segments to use
    for segment in segments_to_use:
        print(segments.index(segment)+1, end=" ")

if __name__ == "__main__":
    main()
