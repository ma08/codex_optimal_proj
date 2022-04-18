import os


class File:
    def __init__(self, path):
        self.path = path

    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __add__(self, other):
        return File(self.path + other.path)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            return f.readline()

    def __str__(self):
        return self.path


file1 = File('test.txt')
file1.write('line1\nline2\nline3')

for line in file1:
    print(ascii(line))

file2 = File('test2.txt')
file2.write('line4\nline5\nline6')

file3 = file1 + file2
print(file3)

print(file3.read())
