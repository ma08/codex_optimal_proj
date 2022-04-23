#!/bin/python3


import sys

def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        if grades[i] >= 38:
            if grades[i] % 5 == 3:
                grades[i] += 2
            elif grades[i] % 5 == 4:
                grades[i] += 1
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
