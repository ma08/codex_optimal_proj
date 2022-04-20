import os
import sys

def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def append_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data)

def create_file(filename):
    with open(filename, 'w') as f:
        pass

def delete_file(filename):
    os.remove(filename)

def main():
    if len(sys.argv) < 2:
        print('Usage: python file.py [create|read|write|append|delete] [filename]')
        sys.exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command == 'create':
        create_file(filename)
    elif command == 'read':
        print(read_file(filename))
    elif command == 'write':
        data = sys.argv[3]
        write_file(filename, data)
    elif command == 'append':
        data = sys.argv[3]
        append_file(filename, data)
    elif command == 'delete':
        delete_file(filename)
    else:
        print('Unknown command: {}'.format(command))

if __name__ == '__main__':
    main()
