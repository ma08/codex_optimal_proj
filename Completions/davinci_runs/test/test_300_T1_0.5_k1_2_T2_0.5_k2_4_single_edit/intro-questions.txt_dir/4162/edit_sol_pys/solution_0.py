
import sys
def main(argv):
    if len(argv) != 2:
        print('usage: python3 {} <input file> <output file>'.format(argv[0]))
        exit()
    with open(argv[1], 'r') as f:
        with open(argv[2], 'w') as g:
            line = f.readline()
            while line:
                g.write(line.upper())
                line = f.readline()
if __name__ == "__main__":
    main(sys.argv)
