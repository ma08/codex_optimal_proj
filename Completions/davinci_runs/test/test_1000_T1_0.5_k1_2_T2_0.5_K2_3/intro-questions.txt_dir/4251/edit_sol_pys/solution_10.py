

"""
Дана матрица чисел размером n×m. Посчитать максимальную разницу между двумя элементами,
стоящими на соседних позициях (различные строки и столбцы), если для каждого столбца
матрицы выполнить сортировку элементов по возрастанию.
"""
def solution(matrix, n, m):
    max_diff = 0
    for row in matrix:
        row.sort()
        for i in range(len(row)-1):
            diff = row[i+1] - row[i]
            if diff > max_diff: max_diff = diff
    return max_diff


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, n, m))
