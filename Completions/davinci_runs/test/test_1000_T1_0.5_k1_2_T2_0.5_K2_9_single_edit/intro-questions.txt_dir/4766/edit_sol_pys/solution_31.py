

import fileinput

num_lines = int(fileinput.input().readline())

for line in fileinput.input():
    if line[:11] == 'Simon says':
        print(line[11:])
