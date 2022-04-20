s = input()
s = s.replace(s[-1], 'es' if s[-1] == 's' else 's')
print(s)


# Can also use the replace function to replace the last character with the plural form 
