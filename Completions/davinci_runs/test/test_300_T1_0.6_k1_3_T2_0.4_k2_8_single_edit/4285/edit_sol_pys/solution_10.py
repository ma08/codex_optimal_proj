import os

class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return file.read()

    def write(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)

    def append(self, content):
        with open(self.file_path, 'a') as file:
            file.write(content)

    def delete(self):
        os.remove(self.file_path)

    def rename(self, new_name):
        os.rename(self.file_path, new_name)
        self.file_path = new_name

    def move(self, new_path):
        new_file = File(new_path)
        new_file.write(self.read())
        self.delete()
        self.file_path = new_path

file = File('test.txt')
file.write('test')
file.append('test2')
print(file.read())
file.rename('test2.txt')
print(file.read())
file.move('test3.txt')
print(file.read())
file.delete()
print(file.read())
