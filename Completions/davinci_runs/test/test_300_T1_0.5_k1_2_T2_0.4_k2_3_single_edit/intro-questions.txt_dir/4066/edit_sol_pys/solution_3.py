

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    min_lcm = lcm(nums[0], nums[1])
    min_i, min_j = 1, 2
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if lcm(nums[i], nums[j]) < min_lcm:
                min_lcm = lcm(nums[i], nums[j])
                min_i, min_j = i + 1, j + 1
    print(min_i, min_j, min_lcm)

if __name__ == '__main__':
    main()
