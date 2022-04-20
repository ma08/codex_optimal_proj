#!/usr/bin/python3

def min_guess(nums):
    if len(nums) == 0:
        return 1
    product = nums[0]
    for i in range(1, len(nums)):
        product *= nums[i]
    product += nums[0]
    for num in nums:
        if product % num != 0:
            return -1
    return product

def main():
    num_queries = int(input())
    for i in range(num_queries):
        num_divisors = int(input())
        divisors = [int(x) for x in input().split()]
        print(min_guess(divisors))

if __name__ == "__main__":
    main()
