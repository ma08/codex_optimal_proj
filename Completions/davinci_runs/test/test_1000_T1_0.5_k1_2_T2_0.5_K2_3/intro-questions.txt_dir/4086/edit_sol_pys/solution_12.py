
from collections import deque 

def main():
    n = int(input())
    nums = [int(input()) for i in range(n)]
    nums = list(dict.fromkeys(nums))    
    print(len(nums), *nums, sep='\n')

main()
