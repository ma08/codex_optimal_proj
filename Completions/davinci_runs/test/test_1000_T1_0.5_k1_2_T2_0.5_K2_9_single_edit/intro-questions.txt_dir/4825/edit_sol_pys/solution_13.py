

import sys
import math

def main():
    #input
    string = sys.stdin.readline().rstrip()

    #process
    output = ""
    for letter in string:
        if letter == "a":
            output += "@"
        elif letter == "b":
            output += "8"
        elif letter == "c":
            output += "("
        elif letter == "d":
            output += "|)"
        elif letter == "e":
            output += "3"
        elif letter == "f":
            output += "#"
        elif letter == "g":
            output += "6"
        elif letter == "h":
            output += "[-]"
        elif letter == "i":
            output += "|"
        elif letter == "j":
            output += "_|"
        elif letter == "k":
            output += "|<"
        elif letter == "l":
            output += "1"
        elif letter == "m":
            output += "[]\\/[]"
        elif letter == "n":
            output += "[]\\[]"
        elif letter == "o":
            output += "0"
        elif letter == "p":
            output += "|D"
        elif letter == "q":
            output += "(,)"
        elif letter == "r":
            output += "|Z"
        elif letter == "s":
            output += "$"
        elif letter == "t":
            output += "']['"
        elif letter == "u":
            output += "|_|"
        elif letter == "v":
            output += "\\/"
        elif letter == "w":
            output += "\\/\\/"
        elif letter == "x":
            output += "}{}"
        elif letter == "y":
            output += "`/"
        elif letter == "z":
            output += "2"
        elif letter == "A":
            output += "@"
        elif letter == "B":
            output += "8"
        elif letter == "C":
            output += "("
        elif letter == "d":
            output += "|)"
        elif letter == "e":
            output += "3"
        elif letter == "f":
            output += "#"
        elif letter == "g":
            output += "6"
        elif letter == "h":
            output += "[-]"
        elif letter == "i":
            output += "|"
        elif letter == "j":
            output += "_|"
        elif letter == "k":
            output += "|<"
        elif letter == "l":
            output += "1"
        elif letter == "m":
            output += "[]\\/[]"
        elif letter == "n":
            output += "[]\\[]"
        elif letter == "o":
            output += "0"
        elif letter == "p":
            output += "|D"
        elif letter == "q":
            output += "(,)"
        elif letter == "r":
            output += "|Z"
        elif letter == "s":
            output += "$"
        elif letter == "t":
            output += "']['"
        elif letter == "u":
            output += "|_|"
        elif letter == "v":
            output += "\\/"
        elif letter == "w":
            output += "\\/\\/"
        elif letter == "x":
            output += "}{}"
        elif letter == "y":
            output += "`/"
        elif letter == "z":
            output += "2"
        else:
            output += letter

    #output
    print(output)

main()
