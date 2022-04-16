

from collections import deque

def main():
    n = int(input())
    nums = deque()
    for i in range(n):
        nums.append(int(input()))
    nums = list(dict.fromkeys(nums)) # создает словарь из последовательности и выводит только уникальные элементы
    print(len(nums))
    print(*nums)

main()
