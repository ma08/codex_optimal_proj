

# Accepts 10 numbers, outputs number of distinct numbers modulo 42
def distinct():
    # Create a list of the 10 numbers
    nums = []
    for i in range(10):
        nums.append(input())
    # Create a list of the 10 numbers modulo 42
    nums_mod = []
    for i in range(10):
        nums_mod.append(nums[i] % 42)
    # Create a set of the 10 numbers modulo 42
    nums_mod_set = set(nums_mod)
    # Output the length of the set
    print(len(nums_mod_set))

# Test the function
distinct()
