

import sys

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # Sort the array in reverse order.
    a.sort(reverse=True)

    # Number of times the largest number in the array is divided by 2.
    ans = 0

    # While the largest number in the array is greater than the kth value.
    while a[0] > a[k-1]:
        # Divide the largest number by 2.
        a[0] //= 2
        # Sort the array in reverse order.
        a.sort(reverse=True)
        # Increment the number of times the largest number in the array is divided by 2.
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
