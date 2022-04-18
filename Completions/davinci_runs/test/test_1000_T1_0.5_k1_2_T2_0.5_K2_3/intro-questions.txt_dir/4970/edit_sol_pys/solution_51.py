

import sys

# MAIN

# Read in the input and store it in a dictionary
# The key is the frosh and the value is the course
froshs = {}

for line in sys.stdin:
    froshs[line] = froshs.get(line, 0) + 1

# Find the most popular combination of courses
# i.e. the highest value in the dictionary
most_popular = max(froshs.values())

# Print the number of frosh who have the most popular combination
print(most_popular)
