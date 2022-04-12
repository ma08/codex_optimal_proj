
import sys
# MAIN

# Read in the input and store it in a dictionary
# The key is the frosh and the value is the course
frosh = {}
for line in sys.stdin:
    frosh[line] = frosh.get(line, 0) + 1
# Find the most popular combination of course
# i.e. the highest value in the dictionary
most_popular = max(frosh.values())
# Print the number of frosh who have the most popular combination
print(most_popular)
