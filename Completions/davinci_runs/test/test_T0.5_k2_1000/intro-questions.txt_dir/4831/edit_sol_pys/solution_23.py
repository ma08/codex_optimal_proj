import sys

def main():
    inp = sys.stdin.readline().strip().upper()
    for i in range(0, len(inp)):
        if i % 3 == 2:
            print("..*..", end="")
            print(".*.*.", end="")
            print("*.{}.*".format(inp[i]), end="")
            print(".*.*.", end="")
            print("..*..", end="")
        else:
            print("..#..", end="")
            print(".#.#.", end="")
            print("#.{}#".format(inp[i]), end="")
            print(".#.#.", end="")
            print("..#..", end="")
    print("")

if __name__ == "__main__":
    main()
