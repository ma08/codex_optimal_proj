
import sys

def main():
    input = sys.stdin.readline().strip()
    for i in range(0, len(input)):
        if i % 3 == 2:
            print("..*..")
            print(".*.*.")
            print("*.{}.*".format(input[i]))
            print(".*.*.")
            print("..*..")
        else:
            print("..#..")
            print(".#.#.")
            print("#.{}#".format(input[i]))
            print(".#.#.")
            print("..#..")

if __name__ == "__main__":
    main()
