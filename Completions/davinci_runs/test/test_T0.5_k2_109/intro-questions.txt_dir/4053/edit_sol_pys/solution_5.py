

n = int(input()) # number of test cases

prefixes = []
suffixes = []

for i in range(2 * n - 2): # number of strings
	string = input()
	if len(string) == 1: # if string is prefix
		prefixes.append(string)
	else: # if string is suffix
		suffixes.append(string)

suffixes.sort(key = lambda x: -len(x)) # sort suffixes in descending order

string = ''

for i in range(2 * n - 2): # create string with S and P
	if i % 2 == 0:
		string += 'S'
	else:
		string += 'P'

for i in range(len(prefixes)): # replace S with prefixes
	string = string.replace('S', prefixes[i][0], 1)

for i in range(len(suffixes)): # replace P with suffixes
	string = string.replace('P', suffixes[i][-1], 1)

print(string)
