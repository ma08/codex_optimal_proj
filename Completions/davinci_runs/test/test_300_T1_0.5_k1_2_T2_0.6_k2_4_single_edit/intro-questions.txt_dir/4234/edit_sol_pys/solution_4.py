

def get_file():
    file_name = input("Enter a file name: ")
    return file_name


def read_file(file_name):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content


def write_file(file_name, content):
    file = open(file_name, "w")
    file.write(content)
    file.close()


def get_text():
    text = input("Enter text to be written to file: ")
    return text


def main():
    file_name = get_file()
    text = get_text()
    write_file(file_name, text)
    file_content = read_file(file_name)
    print(file_content)


if __name__ == '__main__':
    main()
