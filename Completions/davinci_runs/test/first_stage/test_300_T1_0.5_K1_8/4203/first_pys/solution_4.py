

# Get the input string
s = input()

# Check if the first letter is uppercase 'A'
if s[0] == "A":
    # Check if there is exactly one occurrence of 'C' between the third character from the beginning and the second to last character (inclusive)
    if s.count('C') == 1:
        # Check if all letters except the 'A' and 'C' are lowercase
        if s[1:s.index('C')] + s[s.index('C')+1:].islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")