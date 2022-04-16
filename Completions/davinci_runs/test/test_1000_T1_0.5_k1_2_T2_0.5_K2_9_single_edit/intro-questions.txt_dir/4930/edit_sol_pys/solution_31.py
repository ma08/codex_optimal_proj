

s = input().strip()

vowels = ['a', 'e', 'i', 'o', 'u']


if len(s) == 0:
    print(new_s)
    exit()
new_s = ''

i = 0
while i < len(s):
    if s[i] in vowels:
        new_s += s[i]
        i += 2
    else:
        new_s += s[i]
        i += 1

print(new_s)
