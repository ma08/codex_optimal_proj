

from collections import namedtuple, OrderedDict

n = int(input())
cols = input().split(' ')

Student = namedtuple('Student', cols)
students = [Student(*input().split()) for _ in range(n)]

print("{:.2f}".format(sum(float(s.MARKS) for s in students) / n))
