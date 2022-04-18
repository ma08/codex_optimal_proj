
def distinct_modulo_42(nums):
    modulo_nums = [num % 42 for num in nums]
    return len(set(modulo_nums))


def main():
    nums = []
    for i in range(10):
        nums.append(int(input("Enter number {}: ".format(i+1))))
    print(distinct_modulo_42(nums))

if __name__ == "__main__":
    main()
