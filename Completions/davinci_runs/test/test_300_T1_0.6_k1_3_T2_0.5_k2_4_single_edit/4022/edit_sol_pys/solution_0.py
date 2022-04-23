

import math

def find_max_intersection_length(n, segments):
    # Sort segments by starting point
    segments = sorted(segments, key=lambda x: x[0])

    # Find the intersection of all segments
    intersection = [segments[0][0], segments[0][1]]
    for segment in segments:
        if segment[1] < intersection[0]:
            # The segment does not intersect the intersection
            continue
        elif segment[0] > intersection[1]:
            # The segment does not intersect the intersection
            continue
        else:
            # The segment intersects the intersection
            intersection[0] = max(intersection[0], segment[0])
            intersection[1] = min(intersection[1], segment[1])
    intersection_length = intersection[1] - intersection[0]

    # Check each segment for the max length
    max_length = intersection_length
    for segment in segments:
        # Find the intersection of all segments except the current one
        temp_intersection = intersection
        if segment[1] < temp_intersection[0]:
            # The segment does not intersect the intersection
            continue
        elif segment[0] > temp_intersection[1]:
            # The segment does not intersect the intersection
            continue
        else:
            # The segment intersects the intersection
            temp_intersection[0] = max(temp_intersection[0], segment[0])
            temp_intersection[1] = min(temp_intersection[1], segment[1])
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
