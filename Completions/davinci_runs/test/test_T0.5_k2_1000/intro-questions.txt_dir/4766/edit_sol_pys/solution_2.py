
import fileinput

num_lines = int(input())

for line in fileinput.input()[:num_lines+1]:
    if line[:11] == 'Simon says':
        print(line[11:])
