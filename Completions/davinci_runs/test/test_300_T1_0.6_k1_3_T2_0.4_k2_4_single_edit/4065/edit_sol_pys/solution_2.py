import sys



def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def get_max_contest(problemset):
    if len(sys.argv) != 2:
        print("Usage: python3 file.py input.txt")
        sys.exit(1)
    problemset = read_file(sys.argv[1])
    print(get_max_contest(problemset))


if __name__ == "__main__":
    pass
