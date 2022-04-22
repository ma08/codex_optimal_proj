

def median(nums):
    if len(nums) % 2 == 0:  # even
        med = (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
    else:
        med = nums[len(nums)//2]  # odd
    return med

def main():
    n, m = map(float, input().split())  # n is the length of the sequence, m is the median we want to find
    seq = list(map(int, input().split()))  # the sequence of numbers
    c = 0
    for i in range(n):
        for j in range(i, n):
            if median(seq[i:j+1]) == m:
                c += 1
    print(c)

if __name__ == '__main__':
    main()
