import os


def get_file_extension(filename):
    return filename.split('.')[-1]


def get_file_name(filename):
    return filename.split('.')[0]


def get_file_size(filename):
    return os.path.getsize(filename)


def get_file_info(filename):
    return {
        'file_name': get_file_name(filename),
        'file_extension': get_file_extension(filename),
        'file_size': get_file_size(filename)
    }


if __name__ == '__main__':
    file_name = input("Enter file name: ")
    print(get_file_info(file_name))
