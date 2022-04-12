import sys
from collections import defaultdict

def read_ints():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def main():
    n, k = read_ints()
    x = read_ints()
    y = read_ints()
    points = list(zip(x, y))
    points.sort()
    left = [y for x, y in points if x < 0]
    right = [y for x, y in points if x > 0]
    left.sort(reverse=True)
    right.sort(reverse=True)
    i = 0
    j = 0
    ans = 0
    while i < n and j < n:
        if i < len(left) and j < len(right) and left[i] <= right[j]:
            i += 1
            ans += 1
        elif i < len(left):
            i += 1
            ans += 1
        else:
            if j < len(right):
                j += 1
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
