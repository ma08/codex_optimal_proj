
import sys

# MAIN 

# Read in the input and store it in a dictionary 
# The key is the freshman and the value is the courses 
freshman = {}

for line in sys.stdin:
    freshman[line] = freshman.get(line, 0) + 1

# Find the most popular combination of courses 
# i.e. the highest value in the dictionary 
most_popular = max(freshman.values())

# Print the number of freshman who have the most popular combination 
print(most_popular)
