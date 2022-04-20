

import sys

def main():
    line = sys.stdin.readline().strip()
    nums = [int(x) for x in line.split()]
    print(min(nums))
    
main()