

def main():
    # read in the input
    s = input()
    # create the output
    out = ""
    # loop through the input string
    for i in range(len(s)):
        # if the current character is an 'e', add two of them
        if s[i] == 'e':
            out += "ee"
        # otherwise, add the character
        else:
            out += s[i]
    # print the output
    print(out)

main()
