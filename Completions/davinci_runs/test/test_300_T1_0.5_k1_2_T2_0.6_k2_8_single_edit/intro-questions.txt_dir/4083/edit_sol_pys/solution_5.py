

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    # Number of times the largest number in the array is divided by 2.
    ans = 0

    # While the largest number in the array is greater than the desired value.
    while max(a) > a[k-1]:
        # Divide the largest number by 2.
        a[a.index(max(a))] //= 2
        # Increment the number of times the largest number in the array is divided by 2.
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
