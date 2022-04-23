
import sys

def solve(grades):
    final = []
    for grade in grades:
        if grade < 38:
            final.append(grade)
        else:
            if grade % 5 == 0:
                final.append(grade)
            elif grade % 5 >= 3:
                final.append(grade + (5 - grade % 5))
            else:
                final.append(grade)
    return final

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
   grades_t = int(raw_input().strip())
   grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
