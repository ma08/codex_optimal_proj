def pluralize(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'


print(pluralize(input()))
