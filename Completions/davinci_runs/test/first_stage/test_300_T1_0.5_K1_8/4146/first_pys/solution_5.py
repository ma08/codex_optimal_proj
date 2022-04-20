

import sys

def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    # Get the two numbers that appear in the sequence
    nums_set = set(nums)
    nums_set_len = len(nums_set)
    if nums_set_len == 1:
        print(0)
    elif nums_set_len == 2:
        nums_set = list(nums_set)
        nums_set.sort()
        num1 = nums_set[0]
        num2 = nums_set[1]
        # Count the number of each number in the sequence
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            else:
                cnt2 += 1
        # Compare the count of the two numbers and print the smaller one
        print(min(cnt1, cnt2))
    else:
        print(n)

if __name__ == '__main__':
    main()