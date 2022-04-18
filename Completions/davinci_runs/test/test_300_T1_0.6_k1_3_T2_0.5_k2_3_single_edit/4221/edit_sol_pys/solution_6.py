

plural = input()
if plural.endswith('s') or plural.endswith('sh') or plural.endswith('ch') or plural.endswith('x') or plural.endswith('z'):
    plural += 'es'
else:
    plural += 's'
print(plural)
