
import sys

def main():
    text = sys.stdin.readline().strip().split()

    ans = ""
    for word in text:
        for i in range(len(word)):
            if word[i] in "aA":
                ans += "@"
            elif word[i] in "bB":
                ans += "8"
            elif word[i] in "cC":
                ans += "("
            elif word[i] in "dD":
                ans += "|)"
            elif word[i] in "eE":
                ans += "3"
            elif word[i] in "fF":
                ans += "#"
            elif word[i] in "gG":
                ans += "6"
            elif word[i] in "hH":
                ans += "[-]"
            elif word[i] in "iI":
                ans += "|"
            elif word[i] in "jJ":
                ans += "_|"
            elif word[i] in "kK":
                ans += "|<"
            elif word[i] in "lL":
                ans += "1"
            elif word[i] in "mM":
                ans += "[]\\/[]"
            elif word[i] in "nN":
                ans += "[]\\[]"
            elif word[i] in "oO":
                ans += "0"
            elif word[i] in "pP":
                ans += "|D"
            elif word[i] in "qQ":
                ans += "(,)"
            elif word[i] in "rR":
                ans += "|Z"
            elif word[i] in "sS":
                ans += "$"
            elif word[i] in "tT":
                ans += "']['"
            elif word[i] in "uU":
                ans += "|_|"
            elif word[i] in "vV":
                ans += "\\/"
            elif word[i] in "wW":
                ans += "\\/\\/"
            elif word[i] in "xX":
                ans += "}{}"
            elif word[i] in "yY":
                ans += "`/"
            elif word[i] in "zZ":
                ans += "2"
            else:
                ans += word[i]
        ans += " "
    print(ans)

if __name__ == '__main__':
    main()
