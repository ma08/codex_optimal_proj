
import fileinput
num_lines = int(fileinput.input()[0].strip())

for line in fileinput.input()[:num_lines+1]:
    line = line.strip()
    if line[:11] == 'Simon says':
        print(line[11:])
