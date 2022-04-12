

import sys

def main():
    n = read_integer()
    nums = [read_integer() for _ in range(n)]
    result = 0
    for num in nums:
        result += solve(num)
    print(result)
    
def solve(num):
    num = str(num)
    length = len(num)
    if length == 1:
        return int(num)
    return int(num[0])**(length-1) + int(num[1:])

def read_integer():
    return int(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()
