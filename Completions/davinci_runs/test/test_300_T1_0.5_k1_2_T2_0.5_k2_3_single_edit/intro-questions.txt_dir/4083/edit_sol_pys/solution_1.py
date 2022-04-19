

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    # Sort the array in ascending order.
    a.sort()

    # Number of times the largest number in the array is divided by 2.
    ans = 0

    # While the smallest number in the array is less than the desired value.
    while a[0] < a[k-1]:
        # Divide the largest number by 2.
        a[0] *= 2
        # Sort the array in ascending order.
        a.sort()
        # Increment the number of times the largest number in the array is divided by 2.
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
