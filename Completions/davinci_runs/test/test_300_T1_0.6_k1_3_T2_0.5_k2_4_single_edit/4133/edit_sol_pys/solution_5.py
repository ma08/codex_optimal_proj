

import os
import io

def read_file(filename):
    with io.open(filename, "rt", encoding="utf-8") as f:
        return f.read()

def write_file(filename, text):
    with io.open(filename, "wt", encoding="utf-8") as f:
        f.write(text)

def main(filename, text):
    original = read_file(filename)
    write_file(filename, text)
    current = read_file(filename)
    print("Original:")
    print(original)
    print("Current:")
    print(current)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
