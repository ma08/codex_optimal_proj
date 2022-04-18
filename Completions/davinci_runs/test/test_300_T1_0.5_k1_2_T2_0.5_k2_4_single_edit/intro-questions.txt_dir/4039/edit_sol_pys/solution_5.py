

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

def write_file(filename, lines):
    with open(filename, 'w') as f:
        f.writelines(lines)

def sort_lines(lines):
    return sorted(lines)

def main():
    filename = 'file.txt'
    lines = read_file(filename)
    lines = sort_lines(lines)
    write_file(filename, lines)

if __name__ == "__main__":
    main()
