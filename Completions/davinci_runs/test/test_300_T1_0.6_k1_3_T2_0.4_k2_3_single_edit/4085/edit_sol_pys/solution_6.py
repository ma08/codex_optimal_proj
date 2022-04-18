

def min_guess(nums):
    product = 1
    for num in nums:
        product *= num
    for num in nums:
        if product % num != 0 and num != 1:
            return product
    return product + 1

def main():
    num_queries = int(input())
    for i in range(num_queries):
        num_divisors = int(input())
        divisors = [int(x) for x in input().split()]
        print(min_guess(divisors))

if __name__ == "__main__":
    main()
