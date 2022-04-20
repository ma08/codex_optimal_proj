
# SOLUTION


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
