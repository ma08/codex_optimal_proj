def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines


def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


def append_file(file_name, content):
    with open(file_name, 'a') as f:
        f.write(content)
