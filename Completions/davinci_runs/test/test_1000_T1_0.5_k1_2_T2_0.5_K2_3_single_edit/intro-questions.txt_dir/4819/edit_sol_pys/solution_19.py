

def distinct_modulo(nums):
    return len(set([num % 42 for num in nums]))

def main():
    nums = []
    for _ in range(10):
        nums.append(int(input()))
    print(distinct_modulo(nums))

if __name__ == "__main__":
    main()
