
import math

def find_max_intersection_length(n, segments):
    # Sort segments by ending point
    segments = sorted(segments, key = lambda x: x[1])

    # Find the union of all segments
    union = [segments[0][0], segments[0][1]]
    for i in range(1, n):
        if segments[i][0] > union[1]:
            # The segment does not intersect the union
            union[0] = segments[i][0]
            union[1] = segments[i][1]
        elif segments[i][1] > union[1]:
            # The segment intersects the union
            union[1] = segments[i][1]
    union_length = union[1] - union[0]

    # Check each segment for the max length
    max_length = union_length
    for i in range(n):
        # Find the union of all segments except the current one
        temp_union = union
        if segments[i][0] > temp_union[1]:
            # The segment does not intersect the union
            temp_union[0] = segments[i][0]
            temp_union[1] = segments[i][1]
        elif segments[i][1] > temp_union[1]:
            # The segment intersects the union
            temp_union[1] = segments[i][1]
        temp_union_length = temp_union[1] - temp_union[0]
        if temp_union_length > max_length:
            max_length = temp_union_length
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
