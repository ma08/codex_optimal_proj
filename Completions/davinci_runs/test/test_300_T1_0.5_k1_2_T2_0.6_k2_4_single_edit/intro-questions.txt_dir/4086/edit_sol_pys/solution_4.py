
# напишите программу, которая генерирует новый список, в котором каждое значение равно сумме элементов исходного списка на соответствующей позиции
# выведите на экран новый список
# пример ввода:
# 1 2 3 4 5
# пример вывода:
# 15 14 13 12 11
# пример ввода:
# 1 2 3
# пример вывода:
# 6 5 4
a = input().split()
s = 0
for i in range(len(a)):
    s = s + (len(a) - i)
    print(s, end=' ')
