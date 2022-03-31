

n = int(input())

prefixes = []
suffixes = []

for i in range(2 * n - 2):
	string = input()
	if len(string) == 1:
		prefixes.append(string)
	else:
		suffixes.append(string)

suffixes.sort(key = lambda x: -len(x))

string = ''

for i in range(2 * n - 2):
	if i % 2 == 0:
		string += 'P'
	else:
		string += 'S'

for i in range(len(prefixes)):
	string = string.replace('P', prefixes[i][0], 1)

for i in range(len(suffixes)):
	string = string.replace('S', suffixes[i][-1], 1)

print(string)