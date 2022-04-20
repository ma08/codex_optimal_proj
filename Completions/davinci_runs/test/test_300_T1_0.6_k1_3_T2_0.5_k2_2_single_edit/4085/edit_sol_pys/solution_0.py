
def min_guess(nums):
    if len(nums) == 0:
        return 1
    product = 1
    for num in nums:
        product *= num
    product += 1
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
