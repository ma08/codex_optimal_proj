
from collections import deque

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        numbers = [int(x) for x in input().split()]
        max_num = max(numbers)
        min_num = min(numbers)
        print(max_num - min_num)

if __name__ == '__main__':
    main()
