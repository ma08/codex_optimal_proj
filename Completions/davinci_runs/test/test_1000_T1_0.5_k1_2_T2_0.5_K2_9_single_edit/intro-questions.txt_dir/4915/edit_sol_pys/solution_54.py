
import sys

input = sys.stdin.readlines()

log = []
for line in input:
    if line == "-1\n":
        break
    log.append(line.split())

problems = {}
for entry in log:
    problems[entry[1]] = 0

attempts = {}
for entry in log:
    attempts[entry[1]] = 0

times = {}
for entry in log:
    times[entry[1]] = 0

for entry in log:
    if entry[2] == "right":
        problems[entry[1]] += 1
        attempts[entry[1]] += 1
        times[entry[1]] = int(entry[0])
    else:
        attempts[entry[1]] += 1

solved = 0
for problem in problems:
    if problems[problem] == 1:
        solved += 1

timeScore = 0
for problem in problems:
    if problems[problem] == 1:
        timeScore += times[problem]
    else:
        timeScore += (attempts[problem] - 1) * 20

print(solved, timeScore)
