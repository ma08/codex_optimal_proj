

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    nums = [0] * k
    for i in range(n):
        nums[a[i] % k] += 1
    for i in range(k):
        if i == 0:
            ans += nums[0] * (nums[0] - 1) // 2
        elif i == k/2:
            ans += nums[k/2] * (nums[k/2] - 1) // 2
        elif i < k/2:
            ans += nums[i] * nums[k-i]
    return ans

def main():
    print(solve())
    
if __name__ == '__main__':
    main()
