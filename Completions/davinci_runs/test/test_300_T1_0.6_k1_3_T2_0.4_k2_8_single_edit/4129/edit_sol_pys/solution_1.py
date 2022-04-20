import os
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 file.py <file_name> <file_size>")
        sys.exit(1)

    file_name = sys.argv[1]
    file_size = int(sys.argv[2])

    if os.path.isfile(file_name):
        print("File already exists")
        sys.exit(1)

    f = open(file_name, 'wb')
    f.seek(file_size - 1)
    f.write(b'\0')
    f.close()


if __name__ == '__main__':
    main()
