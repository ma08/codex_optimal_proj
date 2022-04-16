"""
file.py
Author: Avery Wallis
Credit: none
Assignment:

Write and submit a program that reads words from the keyboard one at a time until the word "stop" is typed. Then it should print out how many words were entered (not counting "stop"). There should be one print out regardless of how many words are entered.

"""

import sys

    """
    This function takes in words and counts them until the word "stop" is typed
    """
def main():
    words = []
    for line in sys.stdin:
        if line == "stop":
            print(len(words))
            break
        words.append(line)

main()
