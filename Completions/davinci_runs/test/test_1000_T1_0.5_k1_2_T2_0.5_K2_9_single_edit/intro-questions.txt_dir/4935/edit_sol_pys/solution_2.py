from math import cos, sqrt

import sys


def solve(segments, g):
    speeds = []
    for i in range(len(segments)):
        s = segments[i]
        if i == 0:
            speeds.append(sqrt(2 * g * s[0]))
        else:
            speeds.append(sqrt(speeds[i - 1] ** 2 + 2 * g * s[0] * (1 - cos(s[1]))))
    return speeds


if __name__ == '__main__':
    for line in sys.stdin:
        n, g = map(float, line.split())
        segments = []
        for line in sys.stdin:
            segments.append(map(float, line.split()))
            if len(segments) == n:
                break
        print('\n'.join(map(str, solve(segments, g))))
