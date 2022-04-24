

def plural(word):
    if word.endswith('s'):
        return word + 'es'
    else:
        return word + 's'

print(plural(input()))
