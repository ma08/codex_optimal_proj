
import sys

    # Get the number of elements and desired value.
def main():

    # Get the array.
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    # Sort the array in reverse order.
    a.sort(reverse=True)

    # Number of times the largest number in the array is divided by 2.
    ans = 0

    # While the largest number in the array is greater than or equal to the desired value.
    while a[0] > a[k-1]:
        # Divide the largest number by 2.
        a[0] //= 2
        # Sort the array in reverse order.
        a.sort(reverse=True)
        # Increment the number of times the largest number in the array is divided by 2 by 1.
        ans += 1

# Runs the program.
    print(ans)

if __name__ == '__main__':
    main()
