
from fractions import gcd
def gcd(a, b):
    return a * b // gcd(a, b)

def lcm(arr):
    ret = arr[0]
    for i in range(1, len(arr)):
        ret = lcm_ab(ret, arr[i])
    return ret

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    ret = 0
    for i in range(n):
        for j in range(i + 1, n):
            ret = max(ret, (lcm_ab(nums[i], nums[j]) - 1) % nums[i] + (lcm_ab(nums[i], nums[j]) - 1) % nums[j])
    print(ret)

if __name__ == '__main__':
    main()
