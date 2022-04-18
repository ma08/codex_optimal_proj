

import sys

def main():
    # Get input, the first line is a dummy line
    sys.stdin.readline()
    nums = list(map(int, sys.stdin.readline().split()))

    # Sort the numbers in descending order
    nums.sort(reverse=True)

    # Find the sum of the numbers
    sum = 0
    for num in nums:
        sum += num

    # Print the sum
    print(sum)

if __name__ == '__main__':
    main()
