
import sys

def main():
    input = sys.stdin.readline().strip()
    for i in range(0, len(input)):
        if i % 3 == 2:
            print("..*..", end="")
            print(".*.*.", end="")
            print("*.{}.*".format(input[i]), end="")
            print(".*.*.", end="")
            print("..*..", end="")
        else:
            print("..#..", end="")
            print(".#.#.", end="")
            print("#.{}#".format(input[i]), end="")
            print(".#.#.", end="")
            print("..#..", end="")
    print()


if __name__ == "__main__":
    main()
