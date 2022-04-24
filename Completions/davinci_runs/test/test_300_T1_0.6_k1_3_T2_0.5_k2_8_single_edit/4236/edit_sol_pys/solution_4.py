

"""
Дано целое число 1≤n≤10^5 и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие 10^9.
Найдите наибольшую невозрастающую подпоследовательность в A. В первой строке выведите её длину k, во второй — её индексы 1≤i1<i2<…<ik≤n (таким образом, A[i1]≥A[i2]≥…≥A[in]).

Sample Input:
5
5 3 4 4 2
Sample Output:
4
1 3 4 5
"""

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
