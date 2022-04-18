

# The idea is to sort the points by x-coordinate, and then process them in that order.
from itertools import accumulate
import sys

# When processing a point, we maintain a set of all the platforms that have already been placed.

# We can do this in O(log n) time by keeping the platforms sorted by y-coordinate.
# For each platform, we check if the point is above or below it.
# If it's above, we can safely ignore it.

# If it's below, we can add it to a count, and then check if the point is close enough to the platform that we should remove it.
# If we remove it, we also check if the point is close enough to the next platform that we should remove it too.
# This can be done by checking if the y-coordinate of the point plus the length of the platform is greater than the y-coordinate of the next platform.
# If it is, then we remove the next platform as well.

# Otherwise, we keep the platform.

# We then insert the new platform into the set.

# We repeat this process for all the points, and then we're done.
# This runs in O(n log n) time, which is fast enough for the time limit.

def main():
    t = int(sys.stdin.readline()) 
    for _ in range(t):
        n = int(sys.stdin.readline())
        xs = list(map(int, sys.stdin.readline().split())) 
        xs.sort()
        k = int(sys.stdin.readline())
        ds = list(map(int, sys.stdin.readline().split()))
        ds.sort()
        ds.append(0)
        ds.append(0)
        ds = list(accumulate(ds))
        print(xs)
        print(ds)
        for i in range(len(xs)):
            xs[i] += ds[i]
        print(xs)
        xs.sort()
        print(xs)
        print(xs[k])

if __name__ == '__main__':
    main()
