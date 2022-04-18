

import sys
import math

def main():
    input = sys.stdin.readline().strip()
    for i in range(0, len(input), 3):
        if i % 3 == 2:
            print("..*..")
            print(".*.*.")
            print("*.{}.*".format(input[i:i+3]))
            print(".*.*.")
            print("..*..")
        else:
            print("..#..")
            print(".#.#.")
            print("#.{}#".format(input[i:i+3]))
            print(".#.#.")
            print("..#..")

if __name__ == "__main__":
    main()
