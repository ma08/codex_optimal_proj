

# Get input
noun = input()

# Check if noun ends with s
if noun[-1] == 's':
    # If it does, add es
    print(noun + 'es')
else:
    # Otherwise, add s
    print(noun + 's')