

import sys

def get_max_diff(n, m, a, segments, max_diff, num_segments, segments_to_apply):
    # TODO: Implement solution
    return max_diff, num_segments, segments_to_apply

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    segments = []
    for i in range(m):
        segments.append(list(map(int, sys.stdin.readline().split())))

    max_diff, num_segments, segments_to_apply = get_max_diff(n, m, a, segments, 0, 0, [])

    print(max_diff)
    print(num_segments)
    print(*segments_to_apply)
