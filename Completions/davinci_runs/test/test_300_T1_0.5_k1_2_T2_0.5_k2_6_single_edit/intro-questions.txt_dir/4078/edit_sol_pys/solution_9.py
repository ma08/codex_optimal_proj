import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <file>'.format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        print(f.read())
