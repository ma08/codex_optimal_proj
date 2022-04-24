
singular = input()
if singular.endswith('s'):
    plural = singular + 'es'
else:
    plural = singular + 's'
print(plural, singular)
