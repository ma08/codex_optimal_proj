import sys


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    ret = 0
    for i in range(n):
        for j in range(i + 1, n):
            ret = max(ret, (lcm(nums[i], nums[j]) - 1) % nums[i] + (lcm(nums[i], nums[j]) - 1) % nums[j])
    print(ret)

def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == '__main__':
    main()
