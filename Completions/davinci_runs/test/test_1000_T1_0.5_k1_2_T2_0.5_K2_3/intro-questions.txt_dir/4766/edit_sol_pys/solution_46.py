
import fileinput

num_lines = int(fileinput.input()[0]) # get the first line of the file

for line in fileinput.input()[:num_lines]: # iterate over the file
    if line[:11] == 'Simon says':
        print(line[11:])
