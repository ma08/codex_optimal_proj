
import sys

# Read the input
input = sys.stdin.readlines()

# Parse the input
log = []
for line in input:
    if line == "-1\n":
        break
    log.append(line.split())

# Create a dictionary of the problems and the number of times they
# were solved
problems = {}
for entry in log:
    problems[entry[1]] = 0

# Create a dictionary of the problems and the number of times they
# were attempted
attempts = {}
for entry in log:
    attempts[entry[1]] = 0

# Create a dictionary of the problems and the time it took to solve
# them
times = {}
for entry in log:
    times[entry[1]] = 0

# Loop through the log and find out how many problems were solved
# and how many attempts it took to solve them
for entry in log:
    if entry[2] == "right":
        problems[entry[1]] += 1
        attempts[entry[1]] += 1
        times[entry[1]] = int(entry[0])
    else:
        attempts[entry[1]] += 1

# Count the number of problems solved
solved = 0
for problem in problems:
    if problems[problem] == 1:
        solved += 1

# Calculate the time score
timeScore = 0
for problem in problems:
    if problems[problem] == 1:
        timeScore += times[problem]
    else:
        timeScore += (attempts[problem] - 1) * 20

# Print the results
print(solved, timeScore)
