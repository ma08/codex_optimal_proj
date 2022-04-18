

from collections import deque

def main():
    n = int(input())
    nums = deque() # deque is like a list but faster for add or remove elements
    for i in range(n):
        nums.append(int(input())) # add elements to deque
    nums = list(dict.fromkeys(nums)) # remove duplicates using dict
    print(len(nums))
    print(*nums)

main()
