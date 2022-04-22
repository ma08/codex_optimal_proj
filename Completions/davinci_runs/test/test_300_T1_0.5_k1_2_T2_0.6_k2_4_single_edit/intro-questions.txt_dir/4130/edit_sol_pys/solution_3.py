

# SOLUTION
# We can solve this problem with a greedy algorithm.
# First, we sort the array so that the stars are in ascending order.
# Then, we go over the array from left to right.
# If we are at a star that is the same as the previous one,
# we can increase it by one and then we are sure that it will be different from the previous star.
# If we are at a star that is bigger than the previous one by more than one, we can decrease it by one, and we are sure that it will be different from the previous star.
# Otherwise, we can't change the star at all.
# This can be done in linear time, so the overall complexity is O(n).

import sys
readline = sys.stdin.readline

def main():
    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort()
    ans = 1
    prev = a[0]
    for i in range(1, n):
        if a[i] == prev:
            prev += 1
        elif a[i] > prev + 1:
            prev = a[i] - 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
