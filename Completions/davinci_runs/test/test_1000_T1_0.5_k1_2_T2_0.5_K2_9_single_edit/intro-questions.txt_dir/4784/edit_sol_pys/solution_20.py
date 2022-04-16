

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def read_file_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def write_file_lines(filename, data):
    with open(filename, 'w') as f:
        f.writelines(data)

def append_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data)

def append_file_lines(filename, data):
    with open(filename, 'a') as f:
        f.writelines(data)
