

def median(nums, n):
    if len(nums) % 2 == 0:
        med = (nums[n//2] + nums[n//2 - 1]) / 2
    else:
        med = nums[n//2]
    return med

def main():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    c = 0
    for i in range(n):
        for j in range(i, n):
            if median(seq[i:j+1], j+1-i) == m:
                c += 1
    print(c)

if __name__ == '__main__':
    main()
