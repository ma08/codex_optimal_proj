

def distinct(): #Accepts 10 numbers, outputs number of distinct numbers modulo 42
	nums = [] #Create a list of the 10 numbers
	for i in range(10):
		nums.append(input())
	nums_mod = [] #Create a list of the 10 numbers modulo 42
	for i in range(10):
		nums_mod.append(nums[i] % 42)
	nums_mod_set = set(nums_mod) #Create a set of the 10 numbers modulo 42
	print(len(nums_mod_set)) #Output the length of the set

distinct()
