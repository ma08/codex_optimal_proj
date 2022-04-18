
def median(nums):
    if len(nums) % 2 == 0:
        med = nums[len(nums)//2] + nums[len(nums)//2 - 1] / 2
    else:
        med = nums[len(nums)//2]
    return med


def main():
    n, m = map(int, input().split())  # n = length of sequence
    seq = list(map(int, input().split()))  # m = median
    c = 0
    for i in range(n):
        for j in range(i, n):
            if median(seq[i:j+1]) == m:  # check if median of sequence is equal to m
                c += 1
    print(c)

if __name__ == '__main__':
    main()
