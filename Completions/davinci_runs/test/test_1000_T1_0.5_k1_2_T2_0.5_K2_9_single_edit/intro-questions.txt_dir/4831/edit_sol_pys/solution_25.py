
import sys
import math

def main():
    input_str = sys.stdin.readline().strip()
    for i in range(0, len(input_str)):
        if i % 3 == 2:
            print("..*..")
            print(".*.*.")
            print("*.{}.*".format(input_str[i]))
            print(".*.*.")
            print("..*..")
        else:
            print("..#..")
            print(".#.#.")
            print("#.{}#".format(input_str[i]))
            print(".#.#.")
            print("..#..")

if __name__ == "__main__":
    main()
