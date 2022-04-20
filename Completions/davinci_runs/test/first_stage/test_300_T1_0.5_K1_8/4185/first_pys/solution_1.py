

import sys

def get_input():
    n, m = [int(i) for i in input().split()]
    matrix = []
    for i in range(n):
        matrix.append([int(i) for i in input().split()])
    return n, m, matrix


def get_matrix_value(row, column):
    return (row - 1) * m + column


def get_required_value(row, column):
    return matrix[row - 1][column - 1]


def get_required_row(value):
    return (value - 1) // m + 1


def get_required_column(value):
    return (value - 1) % m + 1


def get_move_cost(row, column, value):
    if value == get_matrix_value(row, column):
        return 0
    required_row = get_required_row(value)
    required_column = get_required_column(value)
    if required_row == row:
        return 1
    if required_column == column:
        return 2
    return 3


def get_cost_for_row(row):
    return sum([get_move_cost(row, column, get_required_value(row, column)) for column in range(1, m + 1)])


def get_cost_for_column(column):
    return sum([get_move_cost(row, column, get_required_value(row, column)) for row in range(1, n + 1)])


def get_cost():
    return sum([get_cost_for_row(row) for row in range(1, n + 1)]) + sum([get_cost_for_column(column) for column in range(1, m + 1)])


if __name__ == "__main__":
    n, m, matrix = get_input()
    print(get_cost())