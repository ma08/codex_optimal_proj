from __future__ import print_function
from collections import namedtuple, Counter
from itertools import groupby

N = int(input())
cols = input().split()[1:]

Student = namedtuple('Student', cols)
students = [Student(*input().split()[1:]) for _ in range(N)]

print("{:.2f}".format(sum(float(s.MARKS) for s in students) / len(students)))
