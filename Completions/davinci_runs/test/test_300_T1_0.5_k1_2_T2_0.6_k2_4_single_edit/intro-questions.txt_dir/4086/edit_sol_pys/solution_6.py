from collections import Counter

from collections import deque

def main():
    n = int(input())
    nums = deque()
    for i in range(n):
        nums.append(int(input()))
    nums = Counter(nums)
    print(len(nums.keys()))
    print(*nums.keys())

main()
