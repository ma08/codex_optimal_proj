

import sys
import math

def main():
    # input
    string = sys.stdin.readline().rstrip()

    # process
    output = []
    for letter in string:
        if letter == "a":
            output.append("@")
        elif letter == "b":
            output.append("8")
        elif letter == "c":
            output.append("(")
        elif letter == "d":
            output.append("|)")
        elif letter == "e":
            output.append("3")
        elif letter == "f":
            output.append("#")
        elif letter == "g":
            output += "6"
        elif letter == "h":
            output.append("[-]")
        elif letter == "i":
            output.append("|")
        elif letter == "j":
            output.append("_|")
        elif letter == "k":
            output.append("|<")
        elif letter == "l":
            output += "1"
        elif letter == "m":
            output.append("[]\\/[]")
        elif letter == "n":
            output.append("[]\\[]")
        elif letter == "o":
            output += "0"
        elif letter == "p":
            output.append("|D")
        elif letter == "q":
            output.append("(,)")
        elif letter == "r":
            output.append("|Z")
        elif letter == "s":
            output.append("$")
        elif letter == "t":
            output.append("']['")
        elif letter == "u":
            output.append("|_|")
        elif letter == "v":
            output.append("\\/")
        elif letter == "w":
            output.append("\\/\\/")
        elif letter == "x":
            output += "}{}"
        elif letter == "y":
            output.append("`/")
        elif letter == "z":
            output.append("2")
        elif letter == "A":
            output.append("@")
        elif letter == "B":
            output.append("8")
        elif letter == "C":
            output.append("(")
        elif letter == "D":
            output.append("|)")
        elif letter == "E":
            output.append("3")
        elif letter == "F":
            output.append("#")
        elif letter == "G":
            output += "6"
        elif letter == "H":
            output.append("[-]")
        elif letter == "I":
            output.append("|")
        elif letter == "J":
            output.append("_|")
        elif letter == "K":
            output.append("|<")
        elif letter == "L":
            output += "1"
        elif letter == "M":
            output.append("[]\\/[]")
        elif letter == "N":
            output.append("[]\\[]")
        elif letter == "O":
            output += "0"
        elif letter == "P":
            output.append("|D")
        elif letter == "Q":
            output.append("(,)")
        elif letter == "R":
            output.append("|Z")
        elif letter == "S":
            output.append("$")
        elif letter == "T":
            output.append("']['")
        elif letter == "U":
            output.append("|_|")
        elif letter == "V":
            output.append("\\/")
        elif letter == "W":
            output.append("\\/\\/")
        elif letter == "X":
            output += "}{}"
        elif letter == "Y":
            output.append("`/")
        elif letter == "Z":
            output.append("2")
        else:
            output.append(letter)

    # output
    print("".join(output))

main()
