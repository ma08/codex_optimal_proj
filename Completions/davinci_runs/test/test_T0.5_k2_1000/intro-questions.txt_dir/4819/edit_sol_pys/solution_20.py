
nums = [int(input()) for _ in range(10)]
print(len(set([n % 42 for n in nums])))
