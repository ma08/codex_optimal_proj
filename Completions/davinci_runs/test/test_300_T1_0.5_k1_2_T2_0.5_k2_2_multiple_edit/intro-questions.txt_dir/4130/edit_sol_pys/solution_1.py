

# SOLUTION
# We can use a greedy algorithm to solve this problem.
# The idea is to sort the numbers.
# Then we go over them one by one.
# If we are at a number that is the same as the previous one, we can increase it by one and then we are sure that it will be different from the previous number.
# If we are at a number that is bigger than the previous one by more than one, we can decrease it by one, and we are sure that it will be different from the previous number.
# Otherwise, we can't change the number at all, so we need to add another number.
# We can do this in linear time, so overall complexity is O(n log n).

import sys, math
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
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
