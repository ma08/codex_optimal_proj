

import sys

def get_file_content(file_name):
    with open(file_name, 'r') as f:
        return f.read()

if __name__ == '__main__':
    print(get_file_content(sys.argv[1]))
