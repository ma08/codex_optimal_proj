

# Let's sort the list and then go over it.
# Let's assume that we are at the i-th element in the list.
# If it is the first element, we will just choose it.
# If it is not the first, we will compare it with the previous element.
# If the previous element is bigger, we will choose the current element.
# If the previous element is smaller, we will choose the previous element again.
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
