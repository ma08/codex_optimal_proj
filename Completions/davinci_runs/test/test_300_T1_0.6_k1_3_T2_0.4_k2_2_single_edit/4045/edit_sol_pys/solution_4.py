import os
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print("{} does not exist".format(filename))
        sys.exit(1)

    if os.path.isfile(filename):
        print("{} is a file".format(filename))
    else:
        print("{} is not a file".format(filename))

    if os.path.isdir(filename):
        print("{} is a directory".format(filename))
    else:
        print("{} is not a directory".format(filename))

    if os.path.islink(filename):
        print("{} is a link".format(filename))
    else:
        print("{} is not a link".format(filename))

    if os.path.isabs(filename):
        print("{} is an absolute path".format(filename))
    else:
        print("{} is not an absolute path".format(filename))

    if os.path.isfile(filename):
        print("{} is a file".format(filename))

    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        print("{} is readable".format(filename))

    if os.path.isfile(filename) and os.access(filename, os.W_OK):
        print("{} is writable".format(filename))

    if os.path.isfile(filename) and os.access(filename, os.X_OK):
        print("{} is executable".format(filename))


if __name__ == "__main__":
    main()
