
import sys

def main():
    #input
    userInput = sys.stdin.readline().strip()

    #convert to lowercase
    userInput = userInput.lower()

    #output
    outputString = ""

    #translate each character
    for char in userInput:
        if char == "a":
            outputString += "@"
        elif char == "b":
            outputString += "8"
        elif char == "c":
            outputString += "("
        elif char == "d":
            outputString += "|)"
        elif char == "e":
            outputString += "3"
        elif char == "f":
            outputString += "#"
        elif char == "g":
            outputString += "6"
        elif char == "h":
            outputString += "[-]"
        elif char == "i":
            outputString += "|"
        elif char == "j":
            outputString += "_|"
        elif char == "k":
            outputString += "|<"
        elif char == "l":
            outputString += "1"
        elif char == "m":
            outputString += "[]\\/[]"
        elif char == "n":
            outputString += "[]\\[]"
        elif char == "o":
            outputString += "0"
        elif char == "p":
            outputString += "|D"
        elif char == "q":
            outputString += "(,)"
        elif char == "r":
            outputString += "|Z"
        elif char == "s":
            outputString += "$"
        elif char == "t":
            outputString += "']['"
        elif char == "u":
            outputString += "|_|"
        elif char == "v":
            outputString += "\\/"
        elif char == "w":
            outputString += "\\/\\/"
        elif char == "x":
            outputString += "}{}"
        elif char == "y":
            outputString += "`/"
        elif char == "z":
            outputString += "2"
        else:
            outputString += char

    print(outputString)

main()
