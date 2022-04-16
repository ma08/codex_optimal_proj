
import sys

def read_file(filename):
    """Read a plain text file and return a list of the lines contained"""
    try:
        with open(filename) as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: file {filename} not found")
        sys.exit(2)

def write_file(filename, lines):
    """Write a list of lines to a plain text file"""
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def print_lines(lines):
    """Print a list of lines to the screen"""
    for line in lines:
        print(line)

def main():
    if len(sys.argv) != 3:
        print("Error: expected 2 command line arguments")
        sys.exit(1)

    # read the file
    lines = read_file(sys.argv[1])

    # print the lines to the screen
    print_lines(lines)

    # write the lines to the output file
    write_file(sys.argv[2], lines)

if __name__ == "__main__":
    main()
