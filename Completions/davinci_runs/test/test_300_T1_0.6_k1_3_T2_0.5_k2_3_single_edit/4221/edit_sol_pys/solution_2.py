


def pluralize(word):
    if word.endswith('s'):
        word += 'es'
    else:
        word += 's'
    return word

print(pluralize(input()))
