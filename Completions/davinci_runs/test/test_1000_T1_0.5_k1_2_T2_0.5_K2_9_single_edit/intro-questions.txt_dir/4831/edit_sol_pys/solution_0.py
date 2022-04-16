
import sys

def main():
    inp = sys.stdin.readline().strip()
    for i in range(0, len(inp)):
        if i % 3 == 2:
            print("..*..")
            print(".*.*.")
            print("*.{}.*".format(inp[i]))
            print(".*.*.")
            print("..*..")
        else:
            print("..#..")
            print(".#.#.")
            print("#.{}#".format(inp[i]))
            print(".#.#.")
            print("..#..")

if __name__ == "__main__":
    main()
