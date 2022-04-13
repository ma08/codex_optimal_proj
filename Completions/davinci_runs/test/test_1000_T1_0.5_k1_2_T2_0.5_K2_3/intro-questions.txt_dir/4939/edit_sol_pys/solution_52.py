import sys

def read_file(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    return lines

def write_file(filepath, lines):
    file = open(filepath, 'w')
    file.writelines(lines)
    file.close()

def main():
    lines = read_file(sys.argv[1])
    write_file(sys.argv[2], lines)

if __name__ == '__main__':
    main()
