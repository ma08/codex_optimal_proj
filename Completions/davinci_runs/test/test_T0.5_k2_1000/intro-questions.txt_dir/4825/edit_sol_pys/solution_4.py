

import sys

def main():
    text = sys.stdin.readline().strip() # read line from stdin

    ans = "" # initialize answer

    # iterate through each character in the text
    for i in range(len(text)):
        # if the character is in the string, replace it with the corresponding string
        if text[i] in "aA":
            ans += "@"
        elif text[i] in "bB":
            ans += "8"
        elif text[i] in "cC":
            ans += "("
        elif text[i] in "dD":
            ans += "|)"
        elif text[i] in "eE":
            ans += "3"
        elif text[i] in "fF":
            ans += "#"
        elif text[i] in "gG":
            ans += "6"
        elif text[i] in "hH":
            ans += "[-]"
        elif text[i] in "iI":
            ans += "|"
        elif text[i] in "jJ":
            ans += "_|"
        elif text[i] in "kK":
            ans += "|<"
        elif text[i] in "lL":
            ans += "1"
        elif text[i] in "mM":
            ans += "[]\\/[]"
        elif text[i] in "nN":
            ans += "[]\\[]"
        elif text[i] in "oO":
            ans += "0"
        elif text[i] in "pP":
            ans += "|D"
        elif text[i] in "qQ":
            ans += "(,)"
        elif text[i] in "rR":
            ans += "|Z"
        elif text[i] in "sS":
            ans += "$"
        elif text[i] in "tT":
            ans += "7"
        elif text[i] in "uU":
            ans += "|_|"
        elif text[i] in "vV":
            ans += "\\/"
        elif text[i] in "wW":
            ans += "\\/\\/"
        elif text[i] in "xX":
            ans += "}{}"
        elif text[i] in "yY":
            ans += "`/"
        elif text[i] in "zZ":
            ans += "2"
        else:
            ans += text[i]
    # print the answer
    print(ans)

if __name__ == '__main__':
    main()
