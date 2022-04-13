
import string
import random


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


def get_file_extension(filename):
    file_extension = filename.split(".")[-1]
    print("The extension of the file is : " + file_extension)
    return file_extension


def get_file_size(filename):
    import os
    statinfo = os.stat(filename)
    print("The size of the file is : " + str(statinfo.st_size) + " bytes")
    return statinfo.st_size


def get_file_content(filename):
    with open(filename, "r") as file:
        print("The content of the file is : ")
        print(file.read())


def write_into_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)
        print("The data was written into the file " + filename)


def create_random_file(filename, size):
    data = get_random_string(size)
    write_into_file(filename, data)


def append_into_file(filename, data):
    with open(filename, "a") as file:
        file.write(data)
        print("The data was appended into the file " + filename)


def print_file_info(filename):
    print("The file " + filename + " has the following properties: ")
    print("The extension of the file is: " + get_file_extension(filename))
    print("The size of the file is: " + str(get_file_size(filename)) + " bytes")
    print("The content of the file is: ")
    get_file_content(filename)


def read_file_content(filename):
    with open(filename, "r") as file:
        return file.read()


def copy_file(filename, new_filename):
    data = read_file_content(filename)
    write_into_file(new_filename, data)


def read_file_by_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line)


def read_file_by_chunks(filename):
    with open(filename, "r") as file:
        for chunk in iter(lambda: file.read(10), ""):
            print(chunk)


def get_file_lines_count(filename):
    with open(filename, "r") as file:
        return len(file.readlines())


def get_file_words_count(filename):
    with open(filename, "r") as file:
        return len(file.read().split())

def get_file_chars_count(filename):
    with open(filename, "r") as file:
        return len(file.read())



def main():
    filename = "file.txt"
    new_filename = "new_file.txt"
    data = "Hello World!"
    size = 10
    print_file_info(filename)
    print("\n")
    print("The lines count of the file is: " + str(get_file_lines_count(filename)))
    print("The words count of the file is: " + str(get_file_words_count(filename)))
    print("The chars count of the file is: " + str(get_file_chars_count(filename)))
    print("\n")
    print("The content of the file is: ")
    read_file_by_lines(filename)
    print("\n")
    print("The content of the file is: ")
    read_file_by_chunks(filename)
    print("\n")
    append_into_file(filename, data)
    print("\n")
    print("The content of the file is: ")
    read_file_by_lines(filename)
    print("\n")
    print("The content of the file is: ")
    read_file_by_chunks(filename)
    print("\n")
    copy_file(filename, new_filename)
    print("\n")
    print_file_info(new_filename)
    print("\n")
    create_random_file(filename, size)
    print("\n")
    print_file_info(filename)
    print("\n")


if __name__ == "__main__":
    main()
