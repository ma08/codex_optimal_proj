
import sys

def get_file_name():
    if len(sys.argv) == 1:
        print("No arguments given.")
        return None
    else:
        return sys.argv[1]

def read_file(file_name):
    try:
        file = open(file_name, "r")
        return file
    except FileNotFoundError:
        print("File not found.")
        return None

def print_file(file):
    for line in file:
        print(line)

def main():
    file_name = get_file_name()
    file = read_file(file_name)
    if file:
        print_file(file)

if __name__ == "__main__":
    main()
