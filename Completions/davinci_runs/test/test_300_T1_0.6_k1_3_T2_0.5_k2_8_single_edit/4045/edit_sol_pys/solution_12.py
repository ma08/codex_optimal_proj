import os

def create(path):
    if not os.path.exists(path):
        os.makedirs(path)

def write(path, content):
    with open(path, 'w') as f:
        f.write(content)

def read(path):
    with open(path, 'r') as f:
        return f.read()
