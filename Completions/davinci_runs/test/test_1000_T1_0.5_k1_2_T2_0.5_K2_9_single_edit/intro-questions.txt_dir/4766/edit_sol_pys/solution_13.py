

import fileinput

# num_lines = int(fileinput.input()[0])

for line in fileinput.input():
    if line[:10] == 'Simon says':
        print(line[10:])
