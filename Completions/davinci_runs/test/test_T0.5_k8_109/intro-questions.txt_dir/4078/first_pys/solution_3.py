

import sys

def solve(n, m, a, segments):
    if n == 1:
        return 0, []

    # sort segments by length
    segments.sort(key=lambda s: s[1] - s[0])

    # find min and max elements
    min_a = min(a)
    max_a = max(a)
    min_idx = a.index(min_a)
    max_idx = a.index(max_a)

    # if min and max are in the same segment, then there is no need to choose any segments
    if any(min_idx >= s[0] and min_idx <= s[1] and max_idx >= s[0] and max_idx <= s[1] for s in segments):
        return max_a - min_a, []

    # otherwise, find the segments that contain min and max
    min_segment = None
    max_segment = None
    for s in segments:
        if min_idx >= s[0] and min_idx <= s[1]:
            min_segment = s
        if max_idx >= s[0] and max_idx <= s[1]:
            max_segment = s

    if min_segment is None or max_segment is None:
        raise ValueError("min and max must be in some segment")

    # choose the segments that contain min and max
    chosen_segments = [min_segment, max_segment]
    chosen_segments_idx = [segments.index(s) for s in chosen_segments]

    # apply the chosen segments
    for s in chosen_segments:
        for i in range(s[0] - 1, s[1]):
            a[i] -= 1

    # find new min and max
    new_min_a = min(a)
    new_max_a = max(a)

    return new_max_a - new_min_a, chosen_segments_idx


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    segments = []
    for i in range(m):
        segments.append([int(x) for x in sys.stdin.readline().split()])

    d, chosen_segments_idx = solve(n, m, a, segments)
    print(d)
    print(len(chosen_segments_idx))
    print(' '.join([str(x) for x in chosen_segments_idx]))


if __name__ == '__main__':
    main()