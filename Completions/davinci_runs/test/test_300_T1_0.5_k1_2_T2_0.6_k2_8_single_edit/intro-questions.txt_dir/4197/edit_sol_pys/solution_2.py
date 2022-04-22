
from collections import namedtuple
N, categories = int(input()), input().split()
Student = namedtuple('Student', categories)
marks = [int(Student._make(input().split()).MARKS) for _ in range(N)]
print((sum(marks) / len(marks)))
