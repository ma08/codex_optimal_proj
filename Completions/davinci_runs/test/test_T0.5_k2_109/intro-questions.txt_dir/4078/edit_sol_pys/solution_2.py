

import sys

def read_ints():
    return [int(x) for x in sys.stdin.readline().strip().split()]

def main():
    n, m = read_ints()
    a = read_ints()
    segments = []
    for _ in range(m):
        l, r = read_ints()
        segments.append((l, r))

    min_val = min(a)
    max_val = max(a)
    max_diff = max_val - min_val
    min_diff = max_diff
    max_diff_segments = []
    min_diff_segments = []

    for l, r in segments:
        diff = max(a[l-1:r]) - min(a[l-1:r])
        if diff > min_diff:
            min_diff = diff
            min_diff_segments = [(l, r)]
        elif diff == min_diff:
            min_diff_segments.append((l, r))
        if diff < max_diff:
            max_diff = diff
            max_diff_segments = [(l, r)]
        elif diff == max_diff:
            max_diff_segments.append((l, r))

    print(min_diff, min_diff_segments)
    print(max_diff, max_diff_segments)

    #print(max_val - min_val)
    print(max_val - min_val - min_diff)
    print(len(min_diff_segments))
    for l, r in min_diff_segments:
        print(l, r)

if __name__ == '__main__':
    main()
