
import os
import sys

def main():
    if len(sys.argv) == 1:
        print("usage: file <file>")
        sys.exit()
    else:
        path = sys.argv[1]
        if os.path.isfile(path):
            print("file")
        else:
            print("not a file")

if __name__ == '__main__':
    main()
