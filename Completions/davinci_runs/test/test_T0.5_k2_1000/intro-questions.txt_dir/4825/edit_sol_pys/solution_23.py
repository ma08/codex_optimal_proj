
import sys

def main():
    # inputs
    input = sys.stdin.readline().strip()

    # convert to lower case
    input = input.lower()

    # output
    output = ""

    # translate each character
    for char in input:
        if char == "a":
            output += "@"
        elif char == "b":
            output += "8"
        elif char == "c":
            output += "("
        elif char == "d":
            output += "|)"
        elif char == "e":
            output += "3"
        elif char == "f":
            output += "#"
        elif char == "g":
            output += "6"
        elif char == "h":
            output += "[-]"
        elif char == "i":
            output += "|"
        elif char == "j":
            output += "_|"
        elif char == "k":
            output += "|<"
        elif char == "l":
            output += "1"
        elif char == "m":
            output += "[]\\/[]"
        elif char == "n":
            output += "[]\\[]"
        elif char == "o":
            output += "0"
        elif char == "p":
            output += "|D"
        elif char == "q":
            output += "(,)"
        elif char == "r":
            output += "|Z"
        elif char == "s":
            output += "$"
        elif char == "t":
            output += "']['" 
        elif char == "u":
            output += "|_|"
        elif char == "v":
            output += "\\/"
        elif char == "w":
            output += "\\/\\/"
        elif char == "x":
            output += "}{}"
        elif char == "y":
            output += "`/"
        elif char == "z":
            output += "2"
        else:
            output += char

    print(output)

main()
