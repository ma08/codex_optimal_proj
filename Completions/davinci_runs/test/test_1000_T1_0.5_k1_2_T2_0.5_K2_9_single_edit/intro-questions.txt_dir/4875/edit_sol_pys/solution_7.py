
def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'way'
    for i in range(len(word)):
        if word[i] in 'aeiou':
            return word[i:] + word[:i] + 'ay'
