
import sys
import os


def find_files(path, ext):
    files = []
    for file in os.listdir(path):
        if file.endswith(ext):
            files.append(file)
    return files



def main():
    print(find_files(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
