
import sys

def main():
    string = sys.stdin.readline().strip() # read in the string
    compact = string[0] # start the compact string with the first letter of the string
    for i in range(1, len(string)): # loop through the string
        if string[i] != compact[-1]: # if the current letter is not the same as the last letter of the compact string
            compact += string[i] # add the current letter to the compact string
    print(compact) # print the compact string

main() # call the main function
