

import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.lower().split()
        for i in range(len(line)):
            if line[i] in words:
                line[i] = "."
            words.append(line[i])
        print(" ".join(line), end="")
        print()

main()
