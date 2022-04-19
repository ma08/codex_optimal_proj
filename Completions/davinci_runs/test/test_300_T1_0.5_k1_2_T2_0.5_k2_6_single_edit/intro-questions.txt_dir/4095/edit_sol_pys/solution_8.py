

def median(nums):
    return nums[len(nums)//2]

def main():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    c = 0
    for i in range(n):
        for j in range(i, n):
            if median(seq[i:j+1]) == m:
                c += 1
    print(c)

if __name__ == '__main__':
    main()
