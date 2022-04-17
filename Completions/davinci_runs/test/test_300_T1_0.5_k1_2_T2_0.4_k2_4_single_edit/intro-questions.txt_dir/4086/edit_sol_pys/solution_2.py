
def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(input())
    nums = set(nums)
    print(len(nums))
    print(*nums)

main()
