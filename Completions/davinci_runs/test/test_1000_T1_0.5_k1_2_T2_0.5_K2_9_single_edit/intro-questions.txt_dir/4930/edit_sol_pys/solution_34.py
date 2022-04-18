


def remove_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']

    new_s = ''

    i = 0
    while i < len(s):
        if s[i] in vowels:
            new_s += s[i]
            i += 2
        else:
            new_s += s[i]
            i += 1

    return new_s


s = input()

print(remove_vowels(s))
