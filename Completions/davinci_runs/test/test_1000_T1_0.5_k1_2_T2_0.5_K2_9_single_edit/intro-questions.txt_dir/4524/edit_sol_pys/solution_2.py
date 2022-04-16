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

    def __add__(self, obj):
        new_path = os.path.join(
            os.path.dirname(self.path),
            os.path.basename(self.path) + os.path.basename(obj.path)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())
        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        with open(self.path, 'r') as f:
            return f

    def __next__(self):
        with open(self.path, 'r') as f:
            return next(f)
