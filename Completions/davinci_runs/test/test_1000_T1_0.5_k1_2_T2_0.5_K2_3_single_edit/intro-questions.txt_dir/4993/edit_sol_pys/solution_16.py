

import sys

def main():
    # n, m = map(int, input().split())
    # parts = set()
    # for i in range(m):
    #     parts.add(input())
    #     if len(parts) == n:
    #         print(i+1)
    #         return
    # print('paradox avoided')
    nums = [1,2,3,4]
    for i in nums:
        print(i)
        nums.remove(i)
        print(nums)

if __name__ == '__main__':
    main()
