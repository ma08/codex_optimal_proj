import sys
import os


def main():
    if len(sys.argv) < 2:
        print("Usage: python file.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("%s does not exist" % filename)
        sys.exit(2)

    if os.path.isfile(filename):
        print("%s is a file" % filename)
    else:
        print("%s is not a file" % filename)

    if os.path.isdir(filename):
        print("%s is a directory" % filename)
    else:
        print("%s is not a directory" % filename)

    if os.path.islink(filename):
        print("%s is a link" % filename)
    else:
        print("%s is not a link" % filename)

    if os.path.ismount(filename):
        print("%s is a mount point" % filename)
    else:
        print("%s is not a mount point" % filename)


if __name__ == "__main__":
    main()
