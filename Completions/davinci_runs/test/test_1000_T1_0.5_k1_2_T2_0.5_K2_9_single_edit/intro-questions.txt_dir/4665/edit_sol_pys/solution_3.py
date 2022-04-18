
from collections import namedtuple

n = int(input())
columns = input().split()

student = namedtuple('student', columns)
students = [student(*input().split()) for _ in range(n)]

print("{:.2f}".format(sum(float(s.MARKS) for s in students) / n))
