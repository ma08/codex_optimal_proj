
import sys

def main():
    text = sys.stdin.readline().strip().split()

    ans = ""
    for word in text:
        temp = ""
        for i in range(len(word)):
            if word[i] in "aA": 
                temp += "@"
            elif word[i] in "bB":
                temp += "8"
            elif word[i] in "cC":
                temp += "("
            elif word[i] in "dD":
                temp += "|)"
            elif word[i] in "eE":
                temp += "3"
            elif word[i] in "fF":
                temp += "#"
            elif word[i] in "gG":
                temp += "6"
            elif word[i] in "hH":
                temp += "[-]"
            elif word[i] in "iI":
                temp += "|"
            elif word[i] in "jJ":
                temp += "_|"
            elif word[i] in "kK":
                temp += "|<"
            elif word[i] in "lL":
                temp += "1"
            elif word[i] in "mM":
                temp += "[]\\/[]"
            elif word[i] in "nN":
                temp += "[]\\[]"
            elif word[i] in "oO":
                temp += "0"
            elif word[i] in "pP":
                temp += "|D"
            elif word[i] in "qQ":
                temp += "(,)"
            elif word[i] in "rR":
                temp += "|Z"
            elif word[i] in "sS":
                temp += "$"
            elif word[i] in "tT":
                temp += "']['"
            elif word[i] in "uU":
                temp += "|_|"
            elif word[i] in "vV":
                temp += "\\/"
            elif word[i] in "wW":
                temp += "\\/\\/"
            elif word[i] in "xX":
                temp += "}{}"
            elif word[i] in "yY":
                temp += "`/"
            elif word[i] in "zZ":
                temp += "2"
            else:
                temp += word[i]
        ans += temp + " "
    print(ans)

if __name__ == '__main__':
    main()
