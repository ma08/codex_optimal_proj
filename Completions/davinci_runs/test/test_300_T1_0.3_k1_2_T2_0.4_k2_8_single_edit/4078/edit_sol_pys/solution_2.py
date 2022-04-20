
import sys

def get_max_diff(n, m, a, segments, k):
    # TODO: Implement solution    
    return 0, []

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    k = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    segments = []
    for i in range(m):
        segments.append(list(map(int, sys.stdin.readline().split())))

    max_diff, segments_to_apply = get_max_diff(n, m, a, segments, k)

    print(max_diff)
    print(*segments_to_apply)
