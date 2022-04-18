

#This solution is O(n^2) in time and O(n^2) in space.
def matrix_bombing_plan(m):
    matrix_sum = 0
    for row in m:
        for col in row:
            matrix_sum += col
    matrix_damage = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            matrix_damage += matrix_bombing_plan_helper(m, i, j)
    return matrix_damage - matrix_sum

def matrix_bombing_plan_helper(m, i, j):
    bomb_power = m[i][j]
    matrix_sum = 0
    for row in range(len(m)):
        for col in range(len(m[row])):
            if row == i and col == j:
                matrix_sum += m[row][col] - bomb_power
            elif row == i and col != j:
                matrix_sum += max(m[row][col] - bomb_power, 0)
            elif row != i and col == j:
                matrix_sum += max(m[row][col] - bomb_power, 0)
            else:
                matrix_sum += m[row][col]
    return matrix_sum

import sys
def main():
    m = []
    for line in sys.stdin:
        m.append(list(map(int, line.split())))
    print(matrix_bombing_plan(m))

if __name__ == '__main__':
    main()
