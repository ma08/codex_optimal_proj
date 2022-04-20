
import os


def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def get_file_size(path):
    return os.path.getsize(path)


def get_file_extension(path):
    return os.path.splitext(path)[1]


def main():
    file_list = get_file_list('.')
    for file in file_list:
        print(file, get_file_size(file), get_file_extension(file))

if __name__ == '__main__':
    main()
