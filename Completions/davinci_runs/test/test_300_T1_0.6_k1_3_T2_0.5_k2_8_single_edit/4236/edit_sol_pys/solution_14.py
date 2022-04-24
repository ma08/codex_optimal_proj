

# SOLUTION

# проверка попадания числа в один из интервалов, возвращает True, если попадает
def check(point, interval):
    return interval[0] <= point <= interval[1]

n, m = map(int, input().split())
intervals = []
for i in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))
# перебор всех чисел из интервала [1, m]
points = [i for i in range(1, m + 1)]
# отсеиваем те числа, которые не попадают в один из интервалов
points = [i for i in points if not any(check(i, interval) for interval in intervals)]
print(len(points))
print(*points)
