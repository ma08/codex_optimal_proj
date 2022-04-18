# Задача на программирование: сортировка по последнему знаку
# Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, сколько элементов этой последовательности,
# равны ее наибольшему элементу.
# Sample Input: 1 7 9 0
# Sample Output: 1

list_of_nums = []

while True:
    num = int(input())
    if num == 0:
        break
    list_of_nums.append(num)

print(list_of_nums.count(max(list_of_nums)))
