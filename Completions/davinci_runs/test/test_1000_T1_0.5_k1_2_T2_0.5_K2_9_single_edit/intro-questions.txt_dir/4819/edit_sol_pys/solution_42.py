
#Accepts 10 numbers, outputs number of distinct numbers modulo 42
def distinct():
    #Create a list of the 10 numbers
    nums = [int(input()) for i in range(10)]
    #Create a list of the 10 numbers modulo 42
    nums_mod = [nums[i] % 42 for i in range(10)]
    #Create a set of the 10 numbers modulo 42
    nums_mod_set = set(nums_mod)
    #Output the length of the set
    print(len(nums_mod_set))
