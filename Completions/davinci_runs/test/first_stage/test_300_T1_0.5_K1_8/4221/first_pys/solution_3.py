

# Get the input string
s = input()

# If it ends with 's' then print out the plural form, else just add 's' to the end
if s[-1] == 's':
    print(s + 'es')
else:
    print(s + 's')