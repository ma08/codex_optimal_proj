

def min_guess(nums):
    if len(nums) == 1:
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return nums[0]
        else:
            return -1
        return 1
    product = 1
    for num in nums:
        product *= num
    for num in nums:
        if product % num == 0:
            product += 1
        else:
            return -1
    return product - 1

def main():
    num_queries = int(input())
    for i in range(num_queries):
        num_divisors = int(input())
        divisors = [int(x) for x in input().split()]
        print(min_guess(divisors))

if __name__ == "__main__":
    main()
