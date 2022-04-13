# SOLUTION
# The idea is to sort the weights and then go over them.
# If we are at a weight that is the same as the previous one,
# we can increase it by one, and then we are sure that it will be
# different from the previous weight.
# If we are at a weight that is more than one bigger than the previous one,
# we can decrease it by one, and then we are sure
# that it will be different from the previous weight.
# Otherwise, we can't change the weight at all.
# We can do this in linear time, so overall complexity is O(n).

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
