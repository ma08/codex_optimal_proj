
import sys
import math

def main():
    inputString = sys.stdin.readline().strip()
    for i in range(0, len(inputString)):
        if i % 3 == 2:
            print("..*..")
            print(".*.*.")
            print("*.{}.*".format(inputString[i]))
            print(".*.*.")
            print("..*..")
        else:
            print("..#..")
            print(".#.#.")
            print("#.{}#".format(inputString[i]))
            print(".#.#.")
            print("..#..")

if __name__ == "__main__":
    main()
