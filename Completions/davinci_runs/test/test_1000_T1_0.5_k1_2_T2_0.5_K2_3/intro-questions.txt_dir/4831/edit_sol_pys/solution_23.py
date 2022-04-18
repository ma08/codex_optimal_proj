import sys

def main():
    my_input = sys.stdin.readline().strip()
    for i in range(0, len(my_input)):
        if i % 3 == 2:
            print("..*..")
            print(".*.*.")
            print("*.{}.*".format(my_input[i]))
            print(".*.*.")
            print("..*..")
        else:
            print("..#..")
            print(".#.#.")
            print("#.{}#".format(my_input[i]))
            print(".#.#.")
            print("..#..")

if __name__ == "__main__":
    main()
