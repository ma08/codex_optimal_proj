
from collections import namedtuple

N = int(input())
cols = input().split()

Student = namedtuple('Student', cols)
students = [Student(*input().split()) for _ in range(N)]

print("{:.2f}".format(sum(float(s.MARKS) for s in students) / len(students)))
