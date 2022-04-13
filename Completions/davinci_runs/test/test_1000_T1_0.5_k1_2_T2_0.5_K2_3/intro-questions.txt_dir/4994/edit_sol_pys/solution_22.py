

import sys

def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: python file.py filename")
        sys.exit()
    filename, file_content = args[0], args[1]
    content = read_file(filename)
    write_file(filename, content)

if __name__ == "__main__":
    main()
