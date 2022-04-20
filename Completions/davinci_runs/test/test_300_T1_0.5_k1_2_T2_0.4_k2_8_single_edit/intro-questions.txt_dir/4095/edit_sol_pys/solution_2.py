

def median(nums):
    if len(nums) % 2 == 0:
        med = (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
    else:
        med = nums[len(nums)//2]
    return med

def main():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i, n):
            if median(seq[i:j+1]) == m:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
