
#!/usr/bin/env python3
import sys, os, tempfile
def main(argv):
    if len(argv) != 2:
        print("Usage: {} <file>".format(argv[0]))
        return 1
    filename = argv[1]
    if not os.path.isfile(filename):
        print("{} is not a file".format(filename))
        return 1
    else:
        print("{} is a file".format(filename))
        return 0
if __name__ == '__main__':
    sys.exit(main(sys.argv))
