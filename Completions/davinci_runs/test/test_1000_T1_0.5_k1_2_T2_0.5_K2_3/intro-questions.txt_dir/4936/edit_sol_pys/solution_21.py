


import sys

def main():
    n = int(sys.stdin.readline().strip())
    nums = [int(i) for i in sys.stdin.readline().strip().split()]
    max_nums = []
    for i in range(len(nums) - 2):
        max_nums.append(max(nums[i], nums[i + 1], nums[i + 2]))
    index = max_nums.index(min(max_nums))
    print(index + 1, max_nums[index])


if __name__ == '__main__':
    main()
