
import math

def find_max_intersection_length(n, segments):
    # Sort segments by ending point
    segments = sorted(segments, key = lambda x: x[1])

    # Find the intersection of all segments, starting with the last segment
    intersection = segments[-1]
    for segment in reversed(segments):
        if segment[0] > intersection[0]:
            # The segment intersects the intersection, so add it to the intersection
            intersection[0] = segment[0]

    # Check each segment for the max length, starting with the last segment
    max_length = intersection[1] - intersection[0]
    for segment in segments:
        # Find the intersection of all segments except the current one
        temp_intersection = intersection
        if segment[0] > temp_intersection[0]:
            # The segment intersects the intersection, so add it to the intersection
            temp_intersection[0] = segment[0]
        temp_intersection_length = temp_intersection[1] - temp_intersection[0]
        if temp_intersection_length > max_length:
            max_length = temp_intersection_length
    return max_length

def main():
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = [int(i) for i in input().split()]
        segments.append([l, r])
    print(find_max_intersection_length(n, segments))

if __name__ == '__main__':
    main()
