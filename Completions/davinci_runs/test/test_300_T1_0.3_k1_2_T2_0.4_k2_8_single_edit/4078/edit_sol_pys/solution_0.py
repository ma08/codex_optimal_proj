

import sys

def get_max_diff(n, m, a, segments, k):
    # TODO: Implement solution
    return 0, 0, []

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    k = []
    segments = []
    for i in range(m):
        segments.append(list(map(int, sys.stdin.readline().split())))

    max_diff, num_segments, segments_to_apply = get_max_diff(n, m, a, segments, k)

    print(max_diff)
    print(num_segments)
    print(*segments_to_apply)
