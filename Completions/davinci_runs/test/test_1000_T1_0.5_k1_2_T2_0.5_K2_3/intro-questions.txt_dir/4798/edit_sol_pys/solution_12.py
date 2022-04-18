
# the input is a list of strings
names = input().split('-')

for i in range(len(names)):
    names[i] = names[i][0]

print(''.join(names))
