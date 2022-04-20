import os


class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def write(self, text):
        with open(self.filename, 'w') as f:
            f.write(text)

    def __add__(self, other):
        new_file = File(self.filename + '+' + other.filename)
        new_file.write(self.read() + other.read())
        return new_file

    def __str__(self):
        return self.filename

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.filename, 'r') as f:
            for line in f:
                yield line


if __name__ == '__main__':
    file = File('file.txt')
    file.write('line1\nline2\nline3\n')
    for line in file:
        print(ascii(line))
    print(file.read())
    file2 = File('file2.txt')
    file2.write('line4\nline5\nline6\n')
    print(file2.read())
    new_file = file + file2
    print(new_file)
    print(new_file.read())
