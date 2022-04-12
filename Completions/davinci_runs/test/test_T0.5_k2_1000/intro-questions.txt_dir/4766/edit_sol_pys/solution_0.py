
import fileinput
num_lines = int(fileinput.input()[0].strip())

for line in fileinput.input()[:num_lines]:
    if line.strip()[:11] == 'Simon says':
        print(line.strip()[11:])
