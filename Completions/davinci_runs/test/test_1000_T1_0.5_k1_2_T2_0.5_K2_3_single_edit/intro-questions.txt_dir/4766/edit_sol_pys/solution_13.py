import fileinput

num_lines = int(fileinput.input()[0])

for line in fileinput.input()[:num_lines+1]:
    if line[:11] == 'Simon says':
        print(line[11:])
