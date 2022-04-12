

s = input()  # input string.

vowels = ['a', 'e', 'i', 'o', 'u']  # list of vowels.

new_s = ''  # new string.

i = 0  # index.
while i < len(s):
    if s[i] in vowels:
        new_s += s[i]
        i += 2  # skip next character.
    else:
        new_s += s[i]
        i += 1  # skip next character.

print(new_s)
