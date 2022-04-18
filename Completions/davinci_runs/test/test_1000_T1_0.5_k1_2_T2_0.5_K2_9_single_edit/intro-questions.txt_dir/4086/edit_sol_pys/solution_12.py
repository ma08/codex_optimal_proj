

from collections import deque

def main():
    n = int(input())
    nums = deque()
    for i in range(n):
        nums.append(int(input()))
    nums = list(dict.fromkeys(nums)) # делаем список из словаря, где ключи - элементы списка
    print(len(nums))
    print(*nums)

main()
