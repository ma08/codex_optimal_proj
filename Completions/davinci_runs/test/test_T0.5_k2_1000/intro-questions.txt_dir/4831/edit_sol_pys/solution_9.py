
import sys
import math

def main():
    input_string = sys.stdin.readline().strip()
    for i in range(0, len(input_string)):
        if i % 3 == 2:
            print("..*..")
            print(".*.*.")
            print("*.{}.*".format(input_string[i]))
            print(".*.*.")
            print("..*..")
        else:
            print("..#..")
            print(".#.#.")
            print("#.{}#".format(input_string[i]))
            print(".#.#.")
            print("..#..")

if __name__ == "__main__":
    main()
