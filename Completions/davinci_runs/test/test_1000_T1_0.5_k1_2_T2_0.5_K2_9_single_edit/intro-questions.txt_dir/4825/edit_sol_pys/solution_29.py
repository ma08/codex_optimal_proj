

# Convert input to list of strings
import sys
input = sys.stdin.readlines()

# Set up dictionary
dictionary = {'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3', 'f': '#', 'g': '6', 'h': '[-]', 'i': '|', 'j': '_|', 'k': '|<', 'l': '1', 'm': '[]\/[]', 'n': '[]\[]', 'o': '0', 'p': '|D', 'q': '(,)', 'r': '|Z', 's': '$', 't': '\'][\'', 'u': '|_|', 'v': '\/', 'w': '\/\/', 'x': '}{', 'y': '`/', 'z': '2'}

# Loop through input and replace letters
for line in input:
    for letter in line:
        if letter.lower() in dictionary:
            print(dictionary[letter.lower()], end='')
        else:
            print(letter, end='')
