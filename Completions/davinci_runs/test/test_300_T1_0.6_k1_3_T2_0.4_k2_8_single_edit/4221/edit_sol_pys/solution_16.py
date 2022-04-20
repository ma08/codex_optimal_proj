
singular = input()
plural = singular
if plural.endswith('s'):
    plural += 'es'
else:
    plural += 's'
print(plural)
