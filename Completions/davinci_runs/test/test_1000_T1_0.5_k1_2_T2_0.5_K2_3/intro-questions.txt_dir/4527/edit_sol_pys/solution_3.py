

from sys import stdin

def main():
    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        segments = []
        for j in range(n):
            l, r = [int(x) for x in stdin.readline().split()]
            segments.append([l, r])
        # Sort segments in increasing order of left and right endpoints
        segments.sort()
        # Now, segments are in increasing order of left endpoint
        # and in decreasing order of right endpoint
        # Therefore, we need to reverse the list
        # This is done because we will be using the list in decreasing order of right endpoint
        segments.reverse()
        # Maximum number of non-intersecting segments
        # that are in increasing order of left endpoint
        # and decreasing order of right endpoint
        max_non_intersecting_segments = 0
        # List that contains the right endpoint of the current segment
        # and the maximum number of non-intersecting segments
        # that are in increasing order of left endpoint
        # and decreasing order of right endpoint
        # This list is sorted in increasing order of right endpoint
        right_endpoint_and_max_non_intersecting_segments = []
        for j in range(n):
            # Check if the left endpoint of the current segment
            # is greater than the right endpoint of the last segment
            # in the right_endpoint_and_max_non_intersecting_segments list
            if len(right_endpoint_and_max_non_intersecting_segments) > 0:
                if segments[j][0] > right_endpoint_and_max_non_intersecting_segments[-1][0]:
                    # If yes, then this segment can be added to the list
                    # of non-intersecting segments
                    # Therefore, increase the maximum number of non-intersecting segments
                    # that are in increasing order of left endpoint
                    # and decreasing order of right endpoint
                    max_non_intersecting_segments += 1
                    # Add the right endpoint of the current segment
                    # and the maximum number of non-intersecting segments
                    # that are in increasing order of left endpoint
                    # and decreasing order of right endpoint
                    right_endpoint_and_max_non_intersecting_segments.append([segments[j][1], max_non_intersecting_segments])
                else:
                    # If not, then we need to find the index of the segment
                    # in the right_endpoint_and_max_non_intersecting_segments list
                    # such that the right endpoint of the current segment
                    # is less than or equal to the right endpoint of the segment
                    # in the right_endpoint_and_max_non_intersecting_segments list
                    # and the right endpoint of the current segment
                    # is greater than the right endpoint of the segment
                    # before it in the right_endpoint_and_max_non_intersecting_segments list
                    # This is because the input is given in increasing order of left endpoint
                    # and decreasing order of right endpoint
                    # This is the binary search algorithm
                    # This is done because the list is sorted in increasing order of right endpoint
                    left = 0
                    right = len(right_endpoint_and_max_non_intersecting_segments) - 1
                    while left < right:
                        mid = (left + right) // 2
                        if segments[j][1] > right_endpoint_and_max_non_intersecting_segments[mid][0]:
                            left = mid + 1
                        else:
                            right = mid
                    # This is the index of the segment
                    # in the right_endpoint_and_max_non_intersecting_segments list
                    # such that the right endpoint of the current segment
                    # is less than or equal to the right endpoint of the segment
                    # in the right_endpoint_and_max_non_intersecting_segments list
                    # and the right endpoint of the current segment
                    # is greater than the right endpoint of the segment
                    # before it in the right_endpoint_and_max_non_intersecting_segments list
                    index = right
                    # Check if the left endpoint of the current segment
                    # is greater than the right endpoint of the segment
                    # in the right_endpoint_and_max_non_intersecting_segments list
                    # at the index found above
                    if segments[j][0] > right_endpoint_and_max_non_intersecting_segments[index][0]:
                        # If yes, then this segment can be added to the list
                        # of non-intersecting segments
                        # Therefore, increase the maximum number of non-intersecting segments
                        # that are in increasing order of left endpoint
                        # and decreasing order of right endpoint
                        max_non_intersecting_segments += 1
                        # Add the right endpoint of the current segment
                        # and the maximum number of non-intersecting segments
                        # that are in increasing order of left endpoint
                        # and decreasing order of right endpoint
                        right_endpoint_and_max_non_intersecting_segments.insert(index + 1, [segments[j][1], max_non_intersecting_segments])
                    else:
                        # If not, then this segment cannot be added to the list
                        # of non-intersecting segments
                        # Therefore, increase the maximum number of non-intersecting segments
                        # that are in increasing order of left endpoint
                        # and decreasing order of right endpoint
                        # by the maximum number of non-intersecting segments
                        # that are in increasing order of left endpoint
                        # and decreasing order of right endpoint
                        # of the segment
                        # in the right_endpoint_and_max_non_intersecting_segments list
                        # at the index found above
                        max_non_intersecting_segments += right_endpoint_and_max_non_intersecting_segments[index][1]
            else:
                # If not, then this segment can be added to the list
                # of non-intersecting segments
                # Therefore, increase the maximum number of non-intersecting segments
                # that are in increasing order of left endpoint
                # and decreasing order of right endpoint
                max_non_intersecting_segments += 1
                # Add the right endpoint of the current segment
                # and the maximum number of non-intersecting segments
                # that are in increasing order of left endpoint
                # and decreasing order of right endpoint
                right_endpoint_and_max_non_intersecting_segments.append([segments[j][1], max_non_intersecting_segments])
        # Print the answer
        print(max_non_intersecting_segments)

if __name__ == "__main__":
    main()
