

def main():
    n = int(input()) % 30
    nums = [1, 2, 3, 4, 5, 6]
    for i in range(n):
        nums[i % 5], nums[i % 5 + 1] = nums[i % 5 + 1], nums[i % 5]
    print(''.join(map(str, nums)))

main()
