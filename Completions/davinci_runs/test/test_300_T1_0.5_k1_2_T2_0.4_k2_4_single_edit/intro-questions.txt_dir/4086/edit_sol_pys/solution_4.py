

from collections import deque

def main():
    n = int(input())
    nums = deque()
    for i in range(n):
        nums.append(int(input()))
    nums = list(dict.fromkeys(nums)) # remove duplicates
    print(len(nums)) # print length of list
    print(*nums) # print list

main()
