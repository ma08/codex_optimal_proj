
import sys
import math
def main():
    sequence = sys.stdin.readline().strip()
    substrings = {}
    for i in range(1, len(sequence)):
        for j in range(len(sequence)-i+1):
            substring = sequence[j:j+i]
            if substring in substrings:
                substrings[substring] += 1
            else:
                substrings[substring] = 1
    substrings = sorted(substrings.items(), key=lambda x: x[1], reverse=True)
    macro = substrings[0][0]
    new_sequence = ""
    while macro in sequence:
        new_sequence += "M"
        sequence = sequence.replace(macro, "", 1)
    new_sequence += sequence
    print(len(new_sequence))

main()
