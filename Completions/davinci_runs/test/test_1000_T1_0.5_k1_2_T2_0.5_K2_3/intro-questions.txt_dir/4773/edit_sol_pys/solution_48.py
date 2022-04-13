

import sys
import math

def main():
    sequence = sys.stdin.readline().strip()

    # find the largest possible macro
    # we want to find the largest substring that is repeated at least twice
    # we can do this by counting the number of times each substring occurs
    # and then sorting by the number of occurrences

    # create a dictionary of substrings with their number of occurrences
    substrings = {}
    for i in range(1, len(sequence)):
        for j in range(len(sequence)-i+1):
            substring = sequence[j:j+i]
            if substring in substrings:
                substrings[substring] += 1
            else:
                substrings[substring] = 1

    # sort the substrings by their occurrences
    substrings = sorted(substrings.items(), key=lambda x: x[1], reverse=True)

    # the first substring will be the largest substring that is repeated at least twice
    # so we can use that as our macro
    macro = substrings[0][0]

    # create a new sequence with the macro
    new_sequence = ""
    while macro in sequence:
        new_sequence += "M"
        sequence = sequence.replace(macro, "", 1)
    new_sequence += sequence

    print(len(new_sequence))

main()
