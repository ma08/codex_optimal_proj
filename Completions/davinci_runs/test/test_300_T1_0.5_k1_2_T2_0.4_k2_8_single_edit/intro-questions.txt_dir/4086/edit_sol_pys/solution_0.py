

from collections import deque

def main():
    n = int(input())
    nums = deque()
    for i in range(n):
        nums.append(int(input()))
    nums = list(dict.fromkeys(nums)) #создаем список из словаря, где ключи - элементы входного списка
    print(len(nums)) #выводим количество элементов в новом списке
    print(*nums) #выводим элементы нового списка

main()
