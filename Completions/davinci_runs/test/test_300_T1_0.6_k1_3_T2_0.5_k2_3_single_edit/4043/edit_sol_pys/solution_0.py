
def read_file(file_name):
    with open(file_name) as file:
        return file.read()


def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)


def append_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)


if __name__ == "__main__":
    file_name = 'file.txt'
    content = 'Hello World!'

    write_file(file_name, content)
    print(read_file(file_name))

    append_file(file_name, '\n' + content)
    print(read_file(file_name))
