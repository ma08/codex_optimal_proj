
# input
name = input()
# split and loop
name = name.split('-')
for i in range(len(name)):
    name[i] = name[i][0]
# print
print(''.join(name))
