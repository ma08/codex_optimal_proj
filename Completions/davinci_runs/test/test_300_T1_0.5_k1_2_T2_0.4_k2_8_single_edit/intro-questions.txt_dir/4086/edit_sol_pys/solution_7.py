
from collections import deque

def main():
    n = int(input())
    nums = deque()
    for i in range(n):
        nums.append(int(input()))
    nums = list(dict.fromkeys(nums)) # используем словарь для получения уникальных элементов в очереди
    print(len(nums))
    print(*nums)

main()
