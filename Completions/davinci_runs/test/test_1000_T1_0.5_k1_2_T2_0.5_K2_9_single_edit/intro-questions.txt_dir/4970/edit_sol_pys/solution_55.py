
from collections import Counter

import sys

# MAIN

# Read in the input and store it in a dictionary
# The key is the frosh and the value is the courses
frosh = []

for line in sys.stdin:
    frosh.append(line)

# Find the most popular combination of courses
# i.e. the highest value in the dictionary
most_popular = Counter(frosh).most_common(1)

# Print the number of frosh who have the most popular combination
print(most_popular[0][1])
