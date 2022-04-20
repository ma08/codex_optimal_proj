

import sys

def get_max_diff(n, m, a, segments, dp):
    # TODO: Implement solution
    return 0, 0, [], dp

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]
    segments = []
    for i in range(m):
        segments.append(list(map(int, sys.stdin.readline().split())))

    max_diff, num_segments, segments_to_apply, dp = get_max_diff(n, m, a, segments, dp)

    print(max_diff)
    print(num_segments)
    print(*segments_to_apply)
