
def find_blocks(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1
    else:
        total = sum(nums)
        if total % 2 == 0:
            possible_total = total / 2
            left = 0
            right = len(nums) - 1
            while left != right:
                if nums[left] > possible_total:
                    return 0
                elif nums[left] == possible_total:
                    return 1
                elif sum(nums[left:right]) == possible_total:
                    return 2
                elif sum(nums[left:right]) < possible_total:
                    left += 1
                else:
                    right -= 1
            return 0
        else:
            return 0


def main():
    n = input()
    nums = map(int, raw_input().split())
    blocks = []
    for i in range(n):
        for j in range(i, n):
            result = find_blocks(nums[i:j])
            if result == 2:
                blocks.append([i, j])
    print len(blocks)
    for i in blocks:
        print i[0] + 1, i[1]

main()
