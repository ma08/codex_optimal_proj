

def main():
    # Read in the input.
    s = input()
    # Create the output.
    out = ""
    # Loop through the input string.
    for i in range(len(s)):
        # If the current character is an 'e', add two of them.
        if s[i] == 'i':
            out += "ii"
        # Otherwise, add the character.
        else:
            out += s[i]
    # Print the output.
    print(out)

main()
