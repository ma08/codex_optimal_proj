import os
import sys


class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_file(self):
        try:
            with open(self.filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ''

    def write_file(self, data):
        with open(self.filepath, 'w') as f:
            f.write(data)


class Directory:
    def __init__(self, dirpath):
        self.dirpath = dirpath

    def get_files(self):
        return [os.path.join(self.dirpath, f) for f in os.listdir(self.dirpath) if os.path.isfile(os.path.join(self.dirpath, f))]

    def get_subdirectories(self):
        return [os.path.join(self.dirpath, f) for f in os.listdir(self.dirpath) if os.path.isdir(os.path.join(self.dirpath, f))]


def main():
    if len(sys.argv) < 2:
        print('Usage: python file.py <dirpath>')
        sys.exit(1)

    dirpath = sys.argv[1]
    directory = Directory(dirpath)

    for f in directory.get_files():
        file = File(f)
        data = file.read_file()
        file.write_file(data.upper())


if __name__ == '__main__':
    main()
