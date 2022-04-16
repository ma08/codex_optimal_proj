

import sys, math

# MAIN #

# Get the number of frosh
num_frosh = int(sys.stdin.readline())

# Get the number of courses
num_courses = int(sys.stdin.readline())

# Get the number of frosh who take each course
num_frosh_per_course = []

for line in sys.stdin:
    num_frosh_per_course.append(int(line))

# Get the number of frosh who take each combination of courses
num_frosh_per_combination = []

for i in range(0, num_courses):
    num_frosh_per_combination.append([0] * int(math.pow(2, num_courses)))

for i in range(0, num_frosh):
    # Get the courses that the i-th frosh takes
    frosh_courses = sys.stdin.readline().strip().split()

    # Convert the courses into a number
    num_frosh_courses = 0
    for course in frosh_courses:
        num_frosh_courses += int(math.pow(2, int(course) - 1))

    # Increment the number of frosh who take this combination of courses
    num_frosh_per_combination[len(frosh_courses) - 1][num_frosh_courses] += 1

# Get the number of frosh who take the most popular combination of courses
max_num_frosh = 0

for i in range(0, num_courses):
    max_num_frosh = max(max_num_frosh, max(num_frosh_per_combination[i]))

# Print the number of frosh who take the most popular combination of courses
print(max_num_frosh)
