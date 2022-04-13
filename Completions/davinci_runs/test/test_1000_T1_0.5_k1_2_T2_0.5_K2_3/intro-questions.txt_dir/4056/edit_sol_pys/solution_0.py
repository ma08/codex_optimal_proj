

#!/usr/bin/env python

# import module
import sys

# Grab the filename from the command line
filename = sys.argv[1]

# Open the file
f = open(filename, 'rU')

# Loop over each line
for line in f:
    # Split the line into a list
    line = line.split()
    # Grab the first item in the list and print it
    print line[0]

# Close the file
f.close()
