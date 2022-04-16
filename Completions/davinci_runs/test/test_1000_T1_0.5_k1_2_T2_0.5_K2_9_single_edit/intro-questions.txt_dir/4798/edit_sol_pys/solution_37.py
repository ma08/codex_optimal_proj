

def name_formatter(name):
    name = name.split('-')
    for i in range(len(name)):
        name[i] = name[i][0]

    return ''.join(name)

name = input()

print(name_formatter(name))
