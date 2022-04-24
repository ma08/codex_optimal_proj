

def min_guess(nums, k):
    if len(nums) == 0:
        return 1
    product = 1
    for num in nums:
        product *= num
    product += k
    for num in nums:
        if product % num != 0:
            return -1
    return product

def main():
    num_queries = int(input())
    for i in range(num_queries):
        k = int(input())
        divisors = [int(x) for x in input().split()]
        print(min_guess(divisors, k))

if __name__ == "__main__":
    main()
