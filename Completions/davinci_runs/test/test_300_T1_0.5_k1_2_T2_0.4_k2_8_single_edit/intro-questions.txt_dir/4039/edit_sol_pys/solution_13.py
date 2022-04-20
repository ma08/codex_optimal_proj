
import os
import sys


def get_file_list(search_dir):
    file_list = []
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list


def get_file_list_recursive(search_dir):
    file_list = []
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list


def get_file_list_non_recursive(search_dir):
    file_list = []
    for file in os.listdir(search_dir):
        file_list.append(os.path.join(search_dir, file))

    return file_list


def main():
    if len(sys.argv) < 2:
        print("Usage: python file.py <directory>")
        return

    search_dir = sys.argv[1]
    print("Listing files in directory: %s" % search_dir)

    file_list = get_file_list(search_dir)
    for file in file_list:
        print(file)


if __name__ == "__main__":
    main()
