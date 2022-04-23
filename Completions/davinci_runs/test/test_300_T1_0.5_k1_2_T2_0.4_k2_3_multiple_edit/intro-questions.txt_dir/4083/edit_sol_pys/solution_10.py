
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    # Sort the array in reverse order.
    a.sort(reverse=True)

    # Number of times the smallest number in the array is divided by 2.
    ans = 0

    # While the smallest number in the array is greater than the desired value.
    while a[0] > a[k - 1]:
        # Divide the smallest number by 2.
        a[0] //= 2
        # Sort the array in reverse order.
        a.sort(reverse=True)
        # Increment the number of times the smallest number in the array is divided by 2.
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
