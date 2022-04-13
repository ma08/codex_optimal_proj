
import fileinput
num_lines = int(fileinput.input()[0].rstrip())

for line in fileinput.input()[:num_lines].rstrip():
    if line[:11] == 'Simon says':
        print(line[11:])
