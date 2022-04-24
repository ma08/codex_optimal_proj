

def min_guess(nums):
    product = 1
    for i in range(len(nums)):
        if product % nums[i] != 0:
            product *= nums[i]
    return product + 1

def main():
    num_queries = int(input())
    for i in range(num_queries):
        num_divisors = int(input())
        divisors = [int(x) for x in input().split()]
        print(min_guess(divisors))

if __name__ == "__main__":
    main()
