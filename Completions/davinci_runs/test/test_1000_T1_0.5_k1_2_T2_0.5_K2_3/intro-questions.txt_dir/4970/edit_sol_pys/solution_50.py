

import sys

# MAIN

# Read in the input and store it in a list
# The key is the frosh and the value is the course
froshs = []

for line in sys.stdin:
    froshs.append(line)

# Find the most popular combination of courses
# i.e. the highest value in the dictionary
most_popular = max(froshs)

# Print the number of frosh who have the most popular combination
print(most_popular)
