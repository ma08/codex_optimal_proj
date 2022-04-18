
nums = [int(input()) for i in range(10)] #input
print(len(set([n % 42 for n in nums])))
