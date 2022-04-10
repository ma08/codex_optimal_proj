

def main():
	n = int(input())
	nums = list(map(int, input().split()))
	nums.sort()
	if nums[0] != nums[-1]:
		print("NO")
		return
	if nums[0] == nums[-1]:
		for i in range(1, len(nums)):
			if nums[i] != nums[0]:
				print("NO")
				return
		print("YES")
		for i in range(n):
			print(*[nums[0]]*n)
		return
	print("YES")
	for i in range(n):
		print(*[nums[i*n+j] for j in range(n)])

if __name__ == '__main__':
	main()