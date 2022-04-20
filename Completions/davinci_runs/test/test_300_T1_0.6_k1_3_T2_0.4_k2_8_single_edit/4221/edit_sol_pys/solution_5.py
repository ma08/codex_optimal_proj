

s = input('enter a string: ')

if s[-1] == 's':
    print(s+'es')
else:
    print(s+'s')

# Can also use the replace function to replace the last character with the plural form
# s = s.replace(s[-1], 'es' if s[-1] == 's' else 's')
