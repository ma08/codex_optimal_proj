

import fileinput

num_lines = int(fileinput.input()[0].rstrip())

for line in fileinput.input()[:num_lines]:
    if line.rstrip()[:11] == 'Simon says':
        print(line.rstrip()[11:])
