#%%
nums = [1,2,3,4]
for i in range(len(nums)-1):
    nums.insert(i,nums[i+1])
    print(i,nums)
