import sys

N, A, B = map(int, sys.stdin.readline().rstrip().split())  # input line


def min_expense(N, A, B):  # function to calculate min expense
    if N * A <= B:  # if the cost of all tickets is less than or equal to the cost of a group ticket
        return N * A  # return the cost of all tickets
    else:
        return B  # return the cost of a group ticket



print(min_expense(N, A, B))  # print the result
