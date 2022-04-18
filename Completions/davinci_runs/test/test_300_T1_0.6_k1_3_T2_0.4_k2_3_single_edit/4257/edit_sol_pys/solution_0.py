

import sys, os


def get_file_path(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    return file_path


def main():
    a, b = map(int, sys.stdin.readline().split())
    print(a * b)


if __name__ == '__main__':
    main()
