
from operator import itemgetter
import sys
import math


def solve(N, A, B):
    if N * A <= B:
        return N * A
    else:
        return B


def min_expense(N, A, B):
    if N * A <= B:
        return N * A
    else:
        return B


print(min_expense(N, A, B))
