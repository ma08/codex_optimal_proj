

#!/usr/bin/env python3

# COMPUTING THE MINIMUM INTERVAL LENGTH

# Given n segments on the x-axis of length 1, find the minimum length
# of an interval that contains all the segments.

def min_interval(segments):
    # SOLUTION
    # The problem is to find the segment with the least intersection length.
    # If we sort the segments by their left endpoints, we can consider the
    # problem as finding the segment with the least intersection length with
    # the segment before it.

    # To do this, we can keep track of the right endpoint of the previous
    # segment.  For the first segment, we just set the right endpoint to
    # -infinity.  For the next segment, we compute the intersection length
    # and update the right endpoint to the right endpoint of the current
    # segment.  We can then keep track of the minimum intersection length
    # and return at the end.

    # We can use a heap to keep track of the right endpoint of the previous
    # segment and then just pop the first element, which will be the
    # minimum.

    import heapq

    segments.sort()

    heap = [float('-inf')]
    min_intersection = float('inf')

    for l, r in segments:
        min_intersection = min(min_intersection, heap[0] - l)
        heapq.heappush(heap, r)

    return min_intersection


def main():
    n = int(input())
    segments = []
    for i in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))

    print(min_interval(segments))


if __name__ == '__main__':
    main()
