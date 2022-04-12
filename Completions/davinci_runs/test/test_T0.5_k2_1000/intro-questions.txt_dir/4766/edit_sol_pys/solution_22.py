
# https://open.kattis.com/problems/simonsays
import fileinput

num_lines = int(fileinput.input()[0])

for line in fileinput.input()[:num_lines]:
    if line[:11] == 'Simon says':
        print(line[11:])
