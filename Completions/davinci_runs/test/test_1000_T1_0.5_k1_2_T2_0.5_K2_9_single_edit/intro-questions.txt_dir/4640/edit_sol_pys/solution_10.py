

import sys

# The idea is to sort the points by x-coordinate, and then process them in that order.
# When processing a point, we maintain a set of all the platforms that have already been placed.
# We can do this in O(log n) time by keeping the platforms sorted by y-coordinate.
# For each platform, we check if the point is above or below it.
# If it's above, we can safely ignore it.
# If it's below, we can add it to a count, and then check if the point is close enough to the platform that we should remove it.
# If we remove it, we also check if the point is close enough to the next platform that we should remove it too.
# This can be done by checking if the y-coordinate of the point plus the length of the platform
# is greater than the y-coordinate of the next platform.
# If it is, then we remove the next platform as well.
# Otherwise, we keep the platform.
# We then insert the new platform into the set.
# We repeat this process for all the points, and then we're done.
# This runs in O(n log n) time, which is fast enough for the time limit.

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        xs = list(map(int, sys.stdin.readline().split()))
        ys = list(map(int, sys.stdin.readline().split()))
        points = [(x, y) for x, y in zip(xs, ys)]
        points.sort()
        platforms = []
        count = 0
        for x, y in points:
            while platforms and y > platforms[0][1]:
                platforms.pop(0)
            if not platforms:
                platforms.append((x, y))
                continue
            if y - platforms[0][1] <= k:
                count += 1
                if len(platforms) > 1 and y + k > platforms[1][1]:
                    platforms.pop(0)
                    continue
            platforms.append((x, y))
        print(count)

if __name__ == '__main__':
    main()
