
import fileinput

for line in fileinput.input():
    if line[:11] == 'Simon says':
        print(line[11:])
