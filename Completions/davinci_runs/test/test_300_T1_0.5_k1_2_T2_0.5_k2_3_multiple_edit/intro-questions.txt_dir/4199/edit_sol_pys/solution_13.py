
import os

def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

def read_file(file_name):
    f = open(get_file_path(file_name), "r")
    content = f.read()
    f.close()
    return content

def write_file(file_name, content):
    f = open(get_file_path(file_name), "w")
    f.write(content)
    f.close()
