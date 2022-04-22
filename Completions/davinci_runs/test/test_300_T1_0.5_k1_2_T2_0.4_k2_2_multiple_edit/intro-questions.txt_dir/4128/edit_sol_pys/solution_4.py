
# https://www.codechef.com/problems/FLOW006

def solve(nums):
    return sum(nums)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = [int(x) for x in input().split()]
        print(solve(nums))
