import os

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def write_file(file_name, text):
    with open(file_name, 'w') as f:
        f.write(text)

def append_file(file_name, text):
    with open(file_name, 'a') as f:
        f.write(text)

if os.path.exists('file.txt'):
    print(read_file('file.txt'))
else:
    write_file('file.txt', 'Hello World!')

append_file('file.txt', '\nHello World!')
print(read_file('file.txt'))
