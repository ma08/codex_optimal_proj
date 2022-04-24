from collections import deque

if __name__ == '__main__':
    n = int(input())
    nums = deque()
    for i in range(n):
        nums.append(int(input()))
    nums = list(dict.fromkeys(nums))
    print(len(nums))
    print(*nums)
