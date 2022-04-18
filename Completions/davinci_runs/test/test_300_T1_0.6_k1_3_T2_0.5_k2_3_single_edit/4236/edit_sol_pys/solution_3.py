# Программа должна посчитать количество чисел в диапазоне [1; m], которые не попадают ни в один из интервалов.

# В первой строке входных данных записано два числа n и m — число интервалов и правая граница диапазона, соответственно (1 ≤ n ≤ 100000, 1 ≤ m ≤ 109).

# В следующих n строках записаны по два числа li и ri — координаты концов интервалов (1 ≤ li ≤ ri ≤ m).

# Выведите два числа: количество искомых чисел и сумму искомых чисел.

# Во второй строке выведите через пробел все искомые числа в порядке возрастания.

# Sample Input:

# 2 6
# 2 3
# 5 6

# Sample Output:

# 3 11
# 1 4

# Memory Limit: 256 MB
# Time Limit: 5 seconds

# Code:
# SOLUTION

# проверка попадания числа в один из интервалов
def check(point, intervals):
    for i in intervals:
        if i[0] <= point <= i[1]:
            return True
    return False

n, m = map(int, input().split())
intervals = []
for i in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))
# перебор всех чисел из интервала [1, m]
points = [i for i in range(1, m + 1)]
# отсеиваем те числа, которые попадают в один из интервалов
points = [i for i in points if not check(i, intervals)]
print(len(points))
print(*points)
