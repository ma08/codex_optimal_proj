
# python3

def find_max_intersection_length(n, segments):
    # Sort segments by starting point and find the intersection of all segments
    intersection = [segments[0][0], segments[0][1]]
    for segment in sorted(segments, key = lambda x: x[0]):
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

    # Check each segment for the max length
    max_length = intersection[1] - intersection[0]
    for segment in sorted(segments, key = lambda x: x[0]):
        # Find the intersection of all segments except the current one
        temp_intersection = intersection
        if segment[1] < intersection[0]:
            # The segment does not intersect the intersection
            continue
        elif segment[0] > intersection[1]:
            # The segment does not intersect the intersection
            continue
        else:
            # The segment intersects the intersection
            temp_intersection[0] = max(temp_intersection[0], segment[0])
            temp_intersection[1] = min(temp_intersection[1], segment[1])
        if temp_intersection[1] - temp_intersection[0] > max_length:
            max_length = temp_intersection[1] - temp_intersection[0]
    return max_length

def main():
    n = int(input())
    segments = []
    for _ in range(n):
        segments.append([int(i) for i in input().split()])
    print(find_max_intersection_length(n, segments))

if __name__ == '__main__':
    main()
