import os


def write_file(file_name, text):
    f = open(file_name, 'w')
    f.write(text)
    f.close()


def read_file(file_name):
    f = open(file_name, 'r')
    return f.read()


def main():
    file_name = 'file.txt'
    write_file(file_name, 'Hello world!')
    print(read_file(file_name))


if __name__ == '__main__':
    main()
