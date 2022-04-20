

def plural(noun):
    if noun[-1] == 's':
        return noun + 'es'
    else:
        return noun + 's'

print(plural('cat'))
print(plural('dog'))
