

name = input()

name = name.split('-')
for i in range(len(name)):
    name[i] = name[i][0]

print(''.join(name))
