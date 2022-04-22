

from collections import deque

def main():
    n = int(input())        # n => num of input
    nums = deque()          # nums => nums from input
    for i in range(n):      # append nums to nums
        nums.append(int(input())) 
    nums = list(dict.fromkeys(nums)) # remove duplicated nums
    print(len(nums))        # print length of nums
    print(*nums)            # print nums without brackets

main()
